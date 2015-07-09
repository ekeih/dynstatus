#!/usr/bin/env python3

from subprocess import Popen
from persistent_status import location_changed

def __send_notification(config):
    notify = '\'Name: ' + config['name'] + '\\nStatus: ' + config['statustext'] + '\''
    Popen('notify-send \'Location changed\' ' + notify, shell=True)

def run(config):
    if location_changed(config['name']):
        __send_notification(config)
