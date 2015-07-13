import logging
import network

DEFAULT_POINTS = 10

def __check_ssid(location,ssid):
    if 'ssid' in location:
        if ssid in location['ssid']:
            location['__score'] += DEFAULT_POINTS
            logging.debug('+SSID ==> {}'.format(location['__score']))
        else:
            location['__score'] = -1000
            logging.debug('-SSID ==> {}'.format(location['__score']))

def __check_mac(location,mac):
    if 'mac' in location:
        if mac in location['mac']:
            location['__score'] += DEFAULT_POINTS
            logging.debug('+MAC ==> {}'.format(location['__score']))
        else:
            location['__score'] = -1000
            logging.debug('-MAC ==> {}'.format(location['__score']))

def __check_ip(location,interfaces):
    if 'ip' in location:
        if interfaces[location['interface']] in location['ip']:
            location['__score'] += DEFAULT_POINTS
            logging.debug('+IP ==> {}'.format(location['__score']))
        else:
            location['__score'] = -1000
            logging.debug('-IP ==> {}'.format(location['__score']))


def get_matching_config(config):

    ssid = network.get_ssid_of_accesspoint()
    mac = network.get_mac_of_accesspoint()
    interfaces = network.get_connected_interfaces_and_ip()

    best_config = config.dynstatus['default']
    best_config['__score'] = 0

    for location in config.dynstatus['locations']:
        logging.debug('='*45)
        logging.debug('Checking: {}'.format(location['name']))
        if location['interface'] in interfaces:
            location['__score'] = 0
            __check_ssid(location,ssid)
            __check_mac(location,mac)
            __check_ip(location,interfaces)

            if location['__score'] > best_config['__score']:
                best_config = location
        else:
            logging.debug('Interface not connected.')
    logging.debug('='*45)
    logging.info('Best location: {}'.format(best_config['name']))
    return best_config
