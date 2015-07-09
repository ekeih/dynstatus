#!/usr/bin/env python3

import os
import sys
import glob
import location
import logging

def setup_configuration():
    logging.debug('setup configuration')
    config_path = os.environ.get('XDG_CONFIG_HOME')
    home_path = os.environ.get('HOME')

    if config_path != None:
        config_path = config_path + '/dynstatus'
    elif home_path != None:
        config_path = home_path + '/.config/dynstatus'

    logging.info('config_path %s', config_path)
    if not (os.access(config_path + '/config.py', os.F_OK)):
        logging.error('Config file not found')
        exit()
    else:
        sys.path.append(config_path)
        global config
        import config


def run_plugins():
    logging.debug('run_plugins')
    best_location = location.get_matching_config(config)
    logging.info('Best location: ' + best_location['name'])
    plugins_folder = os.path.expanduser(config.dynstatus['plugins_path'])
    logging.debug('Plugins path: ' + plugins_folder)
    sys.path.append(plugins_folder)
    for plugin in config.dynstatus['plugins']:
        try:
            plugin = __import__(plugin)
            plugin.run(best_location)
        except:
            pass

def run_daemon():
    import time
    logging.info('Running dynstatus in daemon mode.')
    interval = config.dynstatus['daemon_interval']
    logging.info('Interval: %s', interval)
    if os.fork():
        sys.exit()
    while True:
        logging.info('Run plugins')
        run_plugins()
        time.sleep(interval)


def print_help():
    print('TODO: Implement help!')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s: (%(levelname)s) %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.DEBUG)
    logging.debug('=============================================')
    logging.debug('dynstatus v0.1')
    logging.debug('Developed by Max Rosin <dynstatus@hackrid.de>')
    logging.debug('=============================================')
    setup_configuration()

    # argparse
    if len(sys.argv) < 2:
        run_plugins()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'daemon':
            run_daemon()
        else:
            print_help()
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'get':
            best_location = location.get_matching_config(config)
            if sys.argv[2] in best_location:
                print(best_location[sys.argv[2]])
            else:
                print('Unknown value.')
        else:
            print_help()
    else:
        print_help()
