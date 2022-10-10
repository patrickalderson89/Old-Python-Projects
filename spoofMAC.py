#!/usr/bin/python3

import random
import subprocess
import sys


def set_mac():
    new_mac = "00:"
    mac_format = "abcdef1234567890"

    for i in range(1, 11):
        new_mac += random.choice(mac_format)
        if (i % 2 == 0) and (i != 10):
            new_mac += ":"

    return new_mac


def get_mac(interface, func_value):

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", func_value])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

    print(f"New MAC address: {func_value}.")


if __name__ == "__main__":

    ifname = sys.argv[1]
    get_mac(ifname, set_mac())
