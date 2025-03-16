import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%d_%m_%Y')}.log"
log_path=os.path.join(os.getcwd(),'logs')
os.makedirs(log_path,exist_ok=True)


logging.basicConfig(
    filename=os.path.join(log_path,log_file),
    filemode='a',
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
