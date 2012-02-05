import logging
import thread
import threading
import os

threadlock = thread.allocate_lock()

level = logging.DEBUG
LOGGER = logging.getLogger("shopandshare")
LOGGER.setLevel(level)
path = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))
fh = logging.FileHandler( path + "/shopandshare.log")
sh = logging.StreamHandler()
fh.setLevel(level)
sh.setLevel(level)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
LOGGER.addHandler(fh)
LOGGER.addHandler(sh)

def run_thread(message,level):

    global threadlock

    threadlock.acquire()

    if level == logging.DEBUG:
        LOGGER.debug(message)    
    elif level == logging.INFO:
        LOGGER.info(message)
    elif level == logging.ERROR:
        LOGGER.error(message)
    elif level == logging.WARN:
        LOGGER.warn(message)
    
    threadlock.release()

def write(message,level):

    thread.start_new_thread(run_thread,(message.strip(),level))
