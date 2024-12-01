import os 
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"logging.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # Write logs to a file (logs/logging.log)
        logging.StreamHandler(sys.stdout) # output logs to the cmd
    ]
)

logger=logging.getLogger("datasciencelogger")