#!/bin/bash

# Variables
LOCAL_DIR="$HOME/logs"
S3_BUCKET="s3://my-devops-bucket-123456/logs-backup"
LOG_FILE="$HOME/s3_sync.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Sync command
echo "[$DATE] Syncing $LOCAL_DIR to $S3_BUCKET" | tee -a "$LOG_FILE"
aws s3 sync "$LOCAL_DIR" "$S3_BUCKET" --storage-class STANDARD_IA --delete >> "$LOG_FILE" 2>&1

# Check exit status
if [ $? -eq 0 ]; then
    echo "[$DATE] ✅ Sync completed successfully." | tee -a "$LOG_FILE"
else
    echo "[$DATE] ❌ Sync failed." | tee -a "$LOG_FILE"
fi
