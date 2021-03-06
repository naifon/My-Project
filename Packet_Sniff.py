import socket
import struct
import textwrap

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t  '
DATA_TAB_2 = '\t\t  '
DATA_TAB_3 = '\t\t\t  '
DATA_TAB_4 = '\t\t\t\t  '

ETH_P_ALL = 3		# To receive all Ethernet protocols

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))

    with open("packet_sniff.txt","w") as f:
        f.write("")

    while True:
        re=""
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        re+= '\nEthernet Frame:\n'
        re+= TAB_1 + 'Destination: {}, Source: {}, Protocol: {}\n'.format(dest_mac, src_mac, eth_proto)

        # 8 for IPv4
        if eth_proto == 8:
            (version, header_length, ttl, proto,
             src, target, data) = ipv4_packet(data)
            re+= TAB_1 + 'IPv4 Packet:\n'
            re+= TAB_2 + 'Version: {}, Header Length: {}, TTL: {}\n'.format(version, header_length, ttl)
            re+= TAB_2 + 'Protocol: {}, Source: {}, Target: {}\n'.format(proto, src, target)
            # ICMP
            if proto == 1:
                icmp_type, code, checksum, data = icmp_packet(data)
                re+= TAB_1 + 'ICMP Packet:\n'
                re+= TAB_2 + 'Type: {}, Code: {}, Checksum: {},\n'.format(icmp_type, code, checksum)
                re+= TAB_2 + 'Data:\n'
                re+= format_multi_line(DATA_TAB_3, data)

            # TCP
            # Video 7
            elif proto == 6:
                # not sure, data ot data[offset] in next line
                (src_port, dest_port, sequence, acknowledge, flag_urg, flag_ack,
                 flag_psh, flag_rst, flag_syn, flag_fin, data) = tcp_segment(data)
                re+= TAB_1 + 'TCP Segment:\n'
                re+= TAB_2 + 'Source Port: {}, Destination Port: {}\n'.format(src_port, dest_port)
                re+= TAB_2 + 'Sequence: {}, Acknowledge: {}\n'.format(sequence, acknowledge)
                re+= TAB_2 + 'Flags\n'
                # not sure next line
                re+= TAB_3 + 'URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {}\n'.format(
                    flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin)
                re+= TAB_2 + 'Data\n'
                re+= format_multi_line(DATA_TAB_3, data)

            # UDP
            elif proto == 17:
                src_port, dest_port, length, data = udp_segment(data)
                re+= TAB_1 + 'UDP Segment:\n'
                # not sure last length in next line
                re+= TAB_2 + 'Source Port: {}, Destination Port: {}, length: {}\n'.format(
                    src_port, dest_port, length)

            # other
            else:
                re+= TAB_1 + 'Data:\n'
                re+= format_multi_line(DATA_TAB_2, data)
        else:
            re+= 'Data:\n'
            re+= format_multi_line(DATA_TAB_1, data)


        with open("packet_sniff.txt", "a") as f:
            f.write(re)

# unpack ethernet frame


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

# return properly formatted MAC address (ie AA:BB:CC:DD:EE:FF)


def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

# unpacks IPv4 paket


def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x b b 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

# Return properly formatted IPv4 address


def ipv4(addr):
    return '.'.join(map(str, addr))

# Unpack ICMP packet


def icmp_packet(data):

    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

# unpack TCP segment


def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgement,
     offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

# unpack UDP segment


def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

# format multi-line data

def format_multi_line( prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(chr(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


def format_multi_line2(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


main()
