#!/usr/bin/env python3

import dbus

def __connect_to_pidgin():
    try:
        bus = dbus.SessionBus()
        obj = bus.get_object('im.pidgin.purple.PurpleService', '/im/pidgin/purple/PurpleObject')
        pidgin = dbus.Interface(obj, 'im.pidgin.purple.PurpleInterface')
        return pidgin;
    except:
        pass

def __change_status(new_status, new_statustext, dbus_handler):
    try:
        status = dbus_handler.PurpleSavedstatusNew('', new_status)
        dbus_handler.PurpleSavedstatusSetMessage(status, new_statustext)
        dbus_handler.PurpleSavedstatusActivate(status)
    except:
        pass

def run(config):
    try:
        dbus_handler = __connect_to_pidgin()
        statustext = ''
        if 'status_prefix' in config:
            statustext = statustext + config['status_prefix']
        if 'statustext' in config:
            statustext = statustext + config['statustext']
        if 'status_suffix' in config:
            statustext = statustext + config['status_suffix']
        __change_status(config['status'], statustext, dbus_handler)
    except:
        pass
