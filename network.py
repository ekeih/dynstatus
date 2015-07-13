import logging
from subprocess import Popen, PIPE

def get_mac_of_accesspoint():
    command = Popen('iwgetid -ra', shell=True, stdout=PIPE)
    mac = command.stdout.read().decode('utf-8')[:-1]
    logging.debug('MAC of access point: {}'.format(mac))
    return mac

def get_ssid_of_accesspoint():
    command = Popen('iwgetid -r', shell=True, stdout=PIPE)
    ssid = command.stdout.read().decode('utf-8')[:-1]
    logging.debug('SSID of access point: {}'.format(ssid))
    return ssid

def get_connected_interfaces_and_ip():
    command = Popen('ip -f inet addr | grep inet | sed "s/.* \\([0-9]\\{1,3\\}.[0-9]\\{1,3\\}.[0-9]\\{1,3\\}.[0-9]\\{1,3\\}\\)\/.*\\(\\<[a-z]*[0-9]*\\)/\\1 \\2/"', shell=True, stdout=PIPE)
    list_of_interfaces_and_ips = command.stdout.read().decode('utf-8').splitlines()
    interface_ip_pairs = {}
    for pair in list_of_interfaces_and_ips:
        ip,interface = pair.split()
        logging.debug('Iface: {}, IP: {}'.format(interface,ip))
        interface_ip_pairs[interface] = ip
    return interface_ip_pairs
