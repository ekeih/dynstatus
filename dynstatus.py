#!/usr/bin/env python3

import logging
import os
import sys
import glob
import argparse

# TODO move the module in its own namespace
import location

def setup_configuration():
    config_path = os.environ.get('XDG_CONFIG_HOME')
    home_path = os.environ.get('HOME')

    if config_path != None:
        config_path = config_path + '/dynstatus'
    elif home_path != None:
        logging.debug('$XDG_CONFIG_HOME undefined. Fallback to $HOME/.config/')
        config_path = home_path + '/.config/dynstatus'

    logging.debug('config_path {}'.format(config_path))
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
    import importlib
    logging.info('Running dynstatus in daemon mode.')
    interval = config.dynstatus['daemon_interval']
    logging.debug('daemon interval: {}'.format(interval))
    if os.fork():
        sys.exit()
    while True:
        logging.debug('daemon reload config')
        importlib.reload(config)
        run_plugins()
        time.sleep(interval)


def print_help():
    parser.print_help()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dynstatus tries to pinpoint \
        your location based on your network configuration (WLAN, IP, ...) and \
        enables you to run code to react to changes.')
    parser.add_argument(
        '-d',
        '--daemon',
        action='store_true',
        dest='daemon',
        help='Dynstatus will fork to background and detect your location and \
            run your plugins periodically. The interval is configured in the \
            config.py of dynstatus.',
        default=False,
        required=False)
    parser.add_argument(
        '-g',
        '--get',
        help='Dynstatus can give you status information without running the \
            plugins. You can ask for every location setting of your config.py.',
        required=False)
    parser.add_argument(
        '-v',
        '--verbose',
        help='Enable verbose output.',
        action='store_true',
        default=False,
        required=False)
    args = parser.parse_args()

    loglevel = 'INFO'
    if args.verbose:
        loglevel = 'DEBUG'

    logging.basicConfig(
        format='%(asctime)s (%(levelname)s) %(message)s',
        datefmt='%H:%M:%S', level=loglevel)
    #logging.basicConfig(filename='log.txt', level=loglevel)
    logging.debug('='*45)
    logging.debug('dynstatus v0.1')
    logging.debug('Developed by Max Rosin <dynstatus@hackrid.de>')
    logging.debug('='*45)
    setup_configuration()

    # argparse
    if not (args.daemon or args.get):
        run_plugins()
    elif args.daemon:
        run_daemon()
    elif args.get:
        best_location = location.get_matching_config(config)
        if args.get in best_location:
            logging.debug('{}: {}'.format(args.get, best_location[args.get]))
            print(best_location[args.get])
        else:
            logging.error('Unknown value: {}'.format(args.get))
    else:
        print_help()
