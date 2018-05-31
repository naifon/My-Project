# !/usr/bin/env python

import nmap  # import nmap.py module


def main():
    nm = nmap.PortScanner()  # instantiate nmap.PortScanner object

    nm.scan('192.168.0.14', '22-443')  # scan host 127.0.0.1, ports from 22 to 443 // 65535

    nm.command_line()  # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1

    print(nm.scaninfo())  # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}

    print(nm.all_hosts())  # get all hosts that were scanned

    # nm['127.0.0.1'].hostname()          # get one hostname for host 127.0.0.1, usualy the user record

    # nm['127.0.0.1'].hostnames()         # get list of hostnames for host 127.0.0.1 as a list of dict

    # [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]

    # nm['127.0.0.1'].hostname()          # get hostname for host 127.0.0.1

    # nm['127.0.0.1'].state()             # get state of host 127.0.0.1 (up|down|unknown|skipped)

    # nm['127.0.0.1'].all_protocols()     # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)

    # nm['127.0.0.1']['tcp'].keys()       # get all ports for tcp protocol

    # nm['127.0.0.1'].all_tcp()           # get all ports for tcp protocol (sorted version)

    # nm['127.0.0.1'].all_udp()           # get all ports for udp protocol (sorted version)

    # nm['127.0.0.1'].all_ip()            # get all ports for ip protocol (sorted version)

    # nm['127.0.0.1'].all_sctp()          # get all ports for sctp protocol (sorted version)

    # nm['127.0.0.1'].has_tcp(22)         # is there any information for port 22/tcp on host 127.0.0.1

    # nm['127.0.0.1']['tcp'][22]          # get infos about port 22 in tcp on host 127.0.0.1

    # nm['127.0.0.1'].tcp(22)             # get infos about port 22 in tcp on host 127.0.0.1

    # nm['127.0.0.1']['tcp'][22]['state'] # get state of port 22/tcp on host 127.0.0.1 (open

    # a more usefull example :

    re = ""

    for host in nm.all_hosts():

        re += '----------------------------------------------------\n'

        re += 'Host : %s (%s)\n' % (host, nm[host].hostname())

        re += 'State : %s\n' % nm[host].state()

        for proto in nm[host].all_protocols():

            re += '----------\n'

            re += 'Protocol : %s\n' % proto

            lport = nm[host][proto].keys()

            # lport.sort()

            for port in lport:
                re += 'port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state'])

    print(re)

    print('----------------------------------------------------')

    # print result as CSV

    # print(nm.csv())

    exit()

    print('----------------------------------------------------')

    # If you want to do a pingsweep on network 192.168.1.0/24:

    nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')

    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

    print('----------------------------------------------------')

    # Asynchronous usage of PortScannerAsync

    nma = nmap.PortScannerAsync()

    def callback_result(host, scan_result):

        print('------------------')

        print(host, scan_result)

    nma.scan(hosts='192.168.1.0/30', arguments='-sP', callback=callback_result)

    while nma.still_scanning():
        print("Waiting ...")

        nma.wait(2)  # you can do whatever you want but I choose to wait after the end of the scan

    exit()


import socket


def portscan():
    re = ""

    for portno in range(255):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:

            res = s.connect_ex(('localhost', portno))

            if res == 0:
                re += "Port no " + str(portno) + " is open\n"

            # else:

            #     print("Port no " + str(portno) + " is closed")

        except socket.error:

            re = "Could not resolve hostname"

    return re

    # portscan(portno)

