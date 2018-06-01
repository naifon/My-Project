#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2018-05-04 23:58
# @AUTHOR : thang


# import arpreq
try:
    import arpreq
except:
    pass

import atexit
import ipaddress
import logging
import netifaces
import os
import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor
from netifaces import AF_INET

# from core import utils
# from core.constants import THREAD_LIMIT

THREAD_LIMIT = 2


class NetworkScanner:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        pass

    def check_port(self, host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    self.logger.info("Port {}:\tOpen".format(port))
                    return port
        except socket.gaierror:
            self.logger.exception('Hostname could not be resolved')
        except socket.error:
            self.logger.exception("Couldn't connect to server")
        pass

    def scan_ports(self, host):
        """
        SCan all ports of a specific host
        :param host: hostname
        :return: list of futures
        """
        self.logger.debug("Scanning port for host " + host)
        if self.ping_host(host) is None:
            return

        with ThreadPoolExecutor(max_workers=THREAD_LIMIT) as executor:
            futures = []
            open_ports = []
            for port in range(1, 65536):
                future = executor.submit(self.check_port, host, port)
                futures.append(future)

            for future in futures:
                result = future.result()
                if result is not None:
                    open_ports.append(result)
            return open_ports

    def scan_ports_async(self, host, callback=None):
        """
        Callback implementation of scan_ports
        :param host: hostname
        :param callback: on_port_open(port)
        :return: None
        """
        self.logger.debug("Scanning port for host " + host)
        if self.ping_host(host) is None:
            return

        with ThreadPoolExecutor(max_workers=THREAD_LIMIT) as executor:
            futures = []
            for port in range(1, 65536):
                future = executor.submit(self.check_port, host, port)
                futures.append(future)

            for future in futures:
                result = future.result()
                if result is not None and callback:
                    callback(result)

    def ping_host(self, host):
        devnull = open(os.devnull, 'w')
        atexit.register(devnull.close)
        result = subprocess.call(['fping', '-c', '1', '-t', '300', host], stdout=devnull, stderr=devnull)
        if result == 0:
            self.logger.debug("Host {} is up".format(host))
            return host
        else:
            pass

    def ping_sweep(self, network=None):
        if network is None:
            network = self.get_current_network()

        self.logger.debug(network)
        with ThreadPoolExecutor(max_workers=THREAD_LIMIT) as executor:
            futures = []
            online_hosts = []
            for ip in network:
                future = executor.submit(self.ping_host, str(ip))
                futures.append(future)

            for future in futures:
                result = future.result()
                if result is not None:
                    online_hosts.append((result, arpreq.arpreq(result)))
            return online_hosts

    def ping_sweep_async(self, network=None, callback=None):
        if network is None:
            network = self.get_current_network()

        self.logger.debug(network)
        with ThreadPoolExecutor(max_workers=THREAD_LIMIT) as executor:
            futures = []
            for ip in network:
                future = executor.submit(self.ping_host, str(ip))
                futures.append(future)

            for future in futures:
                result = future.result()
                if result is not None and callback:
                    callback((result, arpreq.arpreq(result)))

    def netmask_to_cidr(self, netmask):
        """
        :param netmask: netmask ip addr (eg: 255.255.255.0)
        :return: equivalent cidr number to given netmask ip (eg: 24)
        """
        return sum([bin(int(x)).count('1') for x in netmask.split('.')])

    def get_current_network(self):
        gateways = netifaces.gateways()
        self.logger.debug("gateways = " + str(gateways))
        def_gw_device = gateways['default'][AF_INET][1]
        ifconfig = netifaces.ifaddresses(def_gw_device)[AF_INET][0]
        self.logger.debug("ifconfig = {}".format(ifconfig))
        address = ifconfig['addr']
        net_mask = ifconfig['netmask']
        if_addr = ipaddress.IPv4Interface(address + '/' + str(self.netmask_to_cidr(net_mask)))
        network = if_addr.network
        return network

# res = NetworkScanner().ping_sweep_async()
#
# print(res)
