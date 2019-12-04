import socket
import struct
import textwrap


def ethernet_frame(data):
    """
    Unpack ethernet frame
    Get the src, dest, type and the rest of the data
    """
    dest, src, proto = struct.unpack("! 6s 6s H", data[:14])
    dest_mac = get_mac_addr(dest)
    src_mac = get_mac_addr(src)
    return dest_mac, src_mac, socket.htons(proto), data[14:]


def get_mac_addr(bytes_addr):
    """
    Make MAC address human readable
    >>> get_mac_addr(b'5e\x21\x00r3')
    '35:65:21:00:72:33'
    """
    addr = ":".join("%02x" for b in bytes_addr)
    return addr.upper()


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(655)
        dest, src, proto, payload = ethernet_frame(raw_data)
        print(f"Ethernet Frame\n dest: {dest}\n src: {src}\n proto: {proto}\n")


if __name__ == "__main__":
    print("working")
    main()
