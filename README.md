1. sync local logs to s3
      a. use file sync_local_logs_to_s3.sh
      b. Make it executable: chmod +x sync_local_logs_to_s3.sh
      c. Run ./ync_local_logs_to_s3.sh

2. Using Python Boto3 Upload a file as a Private file
      execute the file upload_private_file.py

3. Python Boto3 generate a signed URL to download the private file
      execute pre-signed_url.py
      output printed will have url

5. Python Backup Script (Local > S3)
     a. write script backup_to_s3.py
     b. Make the Script Executable : chmod +x backup_to_s3.py
     c. Set Up CRON Job (Every Day at 1:00 AM)
         Open crontab editor: crontab -e
         ADD FOLLOWING LINE: 0 1 * * * /usr/bin/python3 /full/path/to/backup_to_s3.py >> /var/log/backup_s3.log 2>&1
