#!/usr/bin/env python3

import os
import tempfile

TEMP_DIRECTORY = tempfile.gettempdir() + '/dynstatus'
STATUS_FILE = TEMP_DIRECTORY + '/status'

def location_changed(name):
    __check_folder()
    with open(STATUS_FILE, 'r') as f:
        status = f.read()
    if status == name:
        return False
    else:
        return True

def __check_folder():
    if not os.path.exists(TEMP_DIRECTORY):
        os.makedirs(TEMP_DIRECTORY)
    if not os.path.isfile(STATUS_FILE):
        with open(STATUS_FILE, 'w') as f:
            f.write('default')

def __write_status(name):
    with open(STATUS_FILE, 'w') as f:
        f.write(name)

def run(config):
    __check_folder()
    __write_status(config['name'])
