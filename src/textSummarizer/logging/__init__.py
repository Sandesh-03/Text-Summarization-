import os
import logging 
import sys

log_str ="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
dir = "logs"
log_file = os.path.join(dir, "running_logs.log")
os.makedirs(dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")
