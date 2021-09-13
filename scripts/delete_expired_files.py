#!/usr/bin/python

from os import listdir
from os.path import isfile, join
import os
import platform
import time 
import logging
from datetime import datetime

PATH_1 = "../src/restapi/static"
PATH_2 = "../src/restapi/files"
LOG_FILE = "logs/deleted_log.log"
MAX_MINUTES = 1410

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def remove_expired(folder_path):

    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for f in files:

        path = join(folder_path, f)
        print(f, creation_date(path))
    
        current = time.time()
        file_creation_minutes = int(round((current - creation_date(path)) / 60))

        print(file_creation_minutes)

        if file_creation_minutes > MAX_MINUTES:
            
            #os.remove(path)

            current_date = datetime.fromtimestamp(current)
            logging.info("Removed file: '" + f + "' on " + str(current_date))


remove_expired(PATH_1)
remove_expired(PATH_2)
