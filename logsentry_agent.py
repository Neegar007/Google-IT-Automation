#!/usr/bin/env python3
"""
LogSentry Agent - Log Collection and Forwarding Agent
Similar to Datadog agent, this agent scans log files and sends them to your platform
"""

import os
import time
import json
import hashlib
import signal
import logging
import argparse
import requests
import configparser
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from collections import deque
import threading


class LogSentryAgent:
    """Main agent class for collecting and forwarding logs"""
    
    def __init__(self, config_path: str = "logsentry.conf"):
        self.config_path = config_path
        self.config = self._load_config()
        self.log_files: Dict[str, dict] = {}
        self.running = False
        self.api_endpoint = self.config.get('api', 'endpoint', fallback='http://localhost:8080/api/logs')
        self.api_key = self.config.get('api', 'api_key', fallback='')
        self.batch_size = self.config.getint('agent', 'batch_size', fallback=10)
        self.flush_interval = self.config.getint('agent', 'flush_interval', fallback=5)
        self.log_buffer: List[dict] = []
        self.setup_logging()
        
    def _load_config(self) -> configparser.ConfigParser:
        """Load configuration from file"""
        config = configparser.ConfigParser()
        if os.path.exists(self.config_path):
            config.read(self.config_path)
        return config
    
    def setup_logging(self):
        """Setup logging for the agent itself"""
        log_level = self.config.get('agent', 'log_level', fallback='INFO')
        logging.basicConfig(
            level=getattr(logging, log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('LogSentry')
        self.logger.info("LogSentry Agent initialized")
    
    def add_log_file(self, file_path: str, file_config: Optional[dict] = None):
        """Add a log file to watch"""
        if not os.path.exists(file_path):
            self.logger.warning(f"Log file does not exist: {file_path}")
            return
            
        file_config = file_config or {}
        self.log_files[file_path] = {
            'path': file_path,
            'position': os.path.getsize(file_path),
            'tags': file_config.get('tags', []),
            'service': file_config.get('service', 'unknown'),
            'source': file_config.get('source', 'file'),
            'encoding': file_config.get('encoding', 'utf-8')
        }
        self.logger.info(f"Added log file to watch: {file_path}")
    
    def read_new_logs(self, file_path: str) -> List[str]:
        """Read new log entries from a file since last read"""
        if file_path not in self.log_files:
            return []
        
        file_info = self.log_files[file_path]
        current_position = file_info['position']
        
        try:
            current_size = os.path.getsize(file_path)
            
            # Handle log rotation (file was truncated or rotated)
            if current_size < current_position:
                self.logger.info(f"Log rotation detected for {file_path}, starting from beginning")
                current_position = 0
            
            if current_size == current_position:
                return []
            
            with open(file_path, 'r', encoding=file_info['encoding']) as f:
                f.seek(current_position)
                new_lines = f.readlines()
                file_info['position'] = f.tell()
                
            return new_lines
            
        except Exception as e:
            self.logger.error(f"Error reading log file {file_path}: {e}")
            return []
    
    def parse_log_entry(self, line: str, file_path: str) -> dict:
        """Parse a log line into a structured format"""
        file_info = self.log_files[file_path]
        
        # Generate unique ID for the log entry
        log_id = hashlib.md5(f"{file_path}:{line}:{time.time()}".encode()).hexdigest()
        
        # Basic log parsing - can be extended for specific formats
        log_entry = {
            'id': log_id,
            'message': line.strip(),
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'source': file_info['source'],
            'service': file_info['service'],
            'tags': file_info['tags'],
            'file_path': file_path
        }
        
        # Try to parse common log formats
        log_entry.update(self._detect_log_format(line))
        
        return log_entry
    
    def _detect_log_format(self, line: str) -> dict:
        """Detect and parse common log formats"""
        result = {'level': 'info', 'parser': 'raw'}
        
        line_lower = line.lower()
        
        # Detect log level
        if 'error' in line_lower or 'err]' in line_lower or 'error:' in line_lower:
            result['level'] = 'error'
        elif 'warn' in line_lower or 'warning' in line_lower:
            result['level'] = 'warning'
        elif 'debug' in line_lower:
            result['level'] = 'debug'
        elif 'critical' in line_lower or 'fatal' in line_lower:
            result['level'] = 'critical'
        elif 'info' in line_lower:
            result['level'] = 'info'
        
        # Try to extract timestamp patterns
        import re
        timestamp_patterns = [
            r'\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}',
            r'\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}',
            r'\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}'
        ]
        
        for pattern in timestamp_patterns:
            match = re.search(pattern, line)
            if match:
                result['extracted_timestamp'] = match.group(0)
                result['parser'] = 'timestamp_detected'
                break
        
        return result
    
    def send_logs_to_platform(self, logs: List[dict]) -> bool:
        """Send logs to the platform API"""
        if not logs:
            return True
            
        payload = {
            'logs': logs,
            'agent_id': self._get_agent_id(),
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'LogSentry/1.0'
        }
        
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
        
        try:
            response = requests.post(
                self.api_endpoint,
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code in (200, 201, 202):
                self.logger.info(f"Successfully sent {len(logs)} logs to platform")
                return True
            else:
                self.logger.error(f"Failed to send logs: {response.status_code} - {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending logs to platform: {e}")
            return False
    
    def _get_agent_id(self) -> str:
        """Get unique agent ID"""
        if not hasattr(self, '_agent_id'):
            host_name = os.environ.get('HOSTNAME', 'unknown')
            self._agent_id = hashlib.md5(f"logsentry-{host_name}".encode()).hexdigest()[:16]
        return self._agent_id
    
    def flush_buffer(self):
        """Flush buffered logs to the platform"""
        if self.log_buffer:
            logs_to_send = self.log_buffer[:self.batch_size]
            if self.send_logs_to_platform(logs_to_send):
                self.log_buffer = self.log_buffer[self.batch_size:]
    
    def process_logs(self):
        """Main log processing loop"""
        while self.running:
            try:
                for file_path in list(self.log_files.keys()):
                    new_lines = self.read_new_logs(file_path)
                    
                    for line in new_lines:
                        if line.strip():  # Skip empty lines
                            log_entry = self.parse_log_entry(line, file_path)
                            self.log_buffer.append(log_entry)
                
                # Flush buffer if it reaches batch size
                if len(self.log_buffer) >= self.batch_size:
                    self.flush_buffer()
                    
            except Exception as e:
                self.logger.error(f"Error in log processing: {e}")
            
            time.sleep(1)
        
        # Final flush when stopping
        self.flush_buffer()
    
    def start(self):
        """Start the agent"""
        self.running = True
        self.logger.info("LogSentry Agent starting...")
        
        # Start the processing thread
        self.process_thread = threading.Thread(target=self.process_logs)
        self.process_thread.daemon = True
        self.process_thread.start()
        
        self.logger.info(f"LogSentry Agent started. Watching {len(self.log_files)} log files.")
    
    def stop(self):
        """Stop the agent"""
        self.logger.info("LogSentry Agent stopping...")
        self.running = False
        if hasattr(self, 'process_thread'):
            self.process_thread.join(timeout=10)
        self.logger.info("LogSentry Agent stopped")
    
    def run_foreground(self):
        """Run agent in foreground (for testing)"""
        self.start()
        try:
            while self.running:
                time.sleep(self.flush_interval)
                self.flush_buffer()
        except KeyboardInterrupt:
            self.stop()


def create_default_config(config_path: str = "logsentry.conf"):
    """Create a default configuration file"""
    config = configparser.ConfigParser()
    
    config['api'] = {
        'endpoint': 'http://localhost:8080/api/logs',
        'api_key': '',
    }
    
    config['agent'] = {
        'log_level': 'INFO',
        'batch_size': '10',
        'flush_interval': '5',
    }
    
    config['logs'] = {
        'paths': '/var/log/syslog,/var/log/messages',
    }
    
    with open(config_path, 'w') as f:
        config.write(f)
    
    print(f"Default configuration created: {config_path}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='LogSentry Agent - Log Collection and Forwarding')
    parser.add_argument('-c', '--config', default='logsentry.conf', help='Configuration file path')
    parser.add_argument('--create-config', action='store_true', help='Create default configuration file')
    parser.add_argument('--add-log', action='append', help='Add log file to watch (can be specified multiple times)')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon')
    parser.add_argument('--foreground', action='store_true', help='Run in foreground (for testing)')
    
    args = parser.parse_args()
    
    if args.create_config:
        create_default_config(args.config)
        return
    
    # Create agent instance
    agent = LogSentryAgent(args.config)
    
    # Add log files from config
    if agent.config.has_section('logs'):
        log_paths = agent.config.get('logs', 'paths', fallback='').split(',')
        for path in log_paths:
            path = path.strip()
            if path:
                agent.add_log_file(path)
    
    # Add log files from command line
    if args.add_log:
        for log_path in args.add_log:
            agent.add_log_file(log_path)
    
    # Handle signals for graceful shutdown
    def signal_handler(signum, frame):
        agent.stop()
        exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    if args.foreground or not args.daemon:
        agent.run_foreground()
    else:
        agent.start()
        # Keep main thread alive
        while agent.running:
            time.sleep(1)


if __name__ == '__main__':
    main()
