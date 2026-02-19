#!/usr/bin/venv python3


def status(cpu, memory, disk):
    checklist =[cpu, memory, disk]
    if not all(isinstance(check, int) for check in checklist):
        return "CRITICAL ERROR! Invalid input detected."
    OK = all(ok < 70 for ok in checklist)
    WARNING = any(warning in range(70,90) for warning in checklist)
    CRITICAL = any(critical >= 90 for critical in checklist)
    
    if CRITICAL and WARNING:
        return "CRITICAL"
    elif CRITICAL:
        return "CRITICAL"
    elif WARNING:
        return "WARNING"
    return "OK"

