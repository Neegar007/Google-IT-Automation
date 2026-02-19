#!/bin/bash

# 1. Create the directory if it doesn't exist
sudo mkdir -p /run/user/$(id -u)

# 2. Set your user as the owner
sudo chown $USER:$USER /run/user/$(id -u)

# 3. Set the required strict permissions (0700)
chmod 0700 /run/user/$(id -u)

# 4. Set the environment variable for the current session
export XDG_RUNTIME_DIR=/run/user/$(id -u)
