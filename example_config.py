#!/usr/bin/env python3

# This is an example configuration. Please copy/move
# it to $XDG_CONFIG_HOME/dynstatus/config.py and
# modify it to your need. On most systems 
# $XDG_CONFIG_HOME will be ~/.config.

# This configuration file will be executed as
# normal python script. So you can use any
# valid python statement to configure dynstatus.

# status codes for pidgin
STATUS_OFFLINE = 1
STATUS_AVAILABLE = 2
STATUS_DO_NOT_DISTURB = 3
# 4 is unknown
STATUS_AWAY = 5
STATUS_EXTENDED_AWAY = 6
# 7 is unknown

dynstatus = {
    # Define where dynstatus can find your plugins.
    # If you want to write your own plugin you just
    # have to put a python script that implements a
    # function 'run(dict)' (where dict will be a
    # dictionary that contains all settings of the
    # matched configuration block) in this folder
    # and enable it in the plugins section.
    'plugins_path' : '~/.config/dynstatus/plugins',

    # Which modules from plugins_path should be executed.
    # Order is important! e.g. persistent_status should
    # be executed as last module.
    'plugins' : ['pidgin', 'notification', 'persistent_status'],

    # If dynstatus runs as daemon all plugins
    # will be executed in this interval (seconds).
    'daemon_interval' : 300,

    # This block is optional. Settings in 'all_locations'
    # will be added to the matching configuration block
    # before the location is passed to the plugins.
    'all_locations' : {
        'status_prefix' : '',
        'status_suffix' : ''
    },

    # You _must_ have a default configuration block.
    # dynstatus will uses these values if no other
    # configuration block matches your current location.
    'default' : {
        'name'          : 'Default',
        'status'        : STATUS_AVAILABLE,
        'statustext'    : ''
    },

    # Put all your location configuration blocks in this dictionary.
    # Every block must have an unique name and an interface.
    # All other settings are optional.
    #
    # You can combine three different filters: ssid, mac and ip.
    # All of them can be a simple string or a python list of strings.
    # ssid : name of a wireless network
    # mac : MAC address of wireless accesspoint
    # ip : local ip address
    #
    # Any additional settings are not used by dynstatus directly.
    # But the complete matching configuration block will be passed
    # to your enabled plugins as dictionary. So you can use them
    # in your plugins. But before you try to access a setting you
    # should make sure that it is available in the passed
    # configuration block.
    'locations' : [
        {
            'name'          : 'Home',
            'interface'     : 'enp0s25',
            'ip'            : '192.168.178.1',
            'status'        : STATUS_DO_NOT_DISTURB,
            'statustext'    : '@Home',
        },
        {
            'name'          : 'University',
            'interface'     : 'wlp3s0',
            'ssid'          :  ['eduroam', 'tub-vpn'],
            'status'        : STATUS_DO_NOT_DISTURB,
            'statustext'    : '@University',
        }
    ]
}
