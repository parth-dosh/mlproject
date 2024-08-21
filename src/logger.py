## any exception that is happening, we should be able to log it and the executions in this file


import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) # gets correct working directory, and then log file
os.makedirs(logs_path, exist_ok = True) # even though there is a file/ folder, keep on appending that whenever we create the file

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # what format we want to use, we are using a generic one
    level = logging.INFO # we want to print these specific messages only when it is info


)



