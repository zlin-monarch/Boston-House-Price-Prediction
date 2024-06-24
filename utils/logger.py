import logging
import os
from time import strftime
from pathlib import Path 


def create_logger():
    log_dir = os.path.join(Path(__file__).parent.parent, 'logs')
    # print('log_dir:', __file__, log_dir)
    os.makedirs(str(log_dir), exist_ok=True)
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    fh = logging.FileHandler(log_dir + '/' + strftime("%H_%M_%m_%d_%Y.log"))
    logger.addHandler(fh)
    return logger

