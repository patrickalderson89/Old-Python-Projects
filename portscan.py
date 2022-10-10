#!/usr/bin/python3

import sys
import nmap
from time import sleep
from stringcolor import cs, bold

help_msg = f"\nSyntax:\n\t{sys.argv[0]} <ip> <ports[port1 port2 port3]> (optional)\n"

if len(sys.argv) < 2 or str(sys.argv[1]) == "--help":
    print(help_msg)
    sys.exit(1)

target = sys.argv[1]

ports = []
for i in range(2, len(sys.argv)):
    ports.append(int(sys.argv[i]))

if len(ports) < 1:
    ports = [21, 22, 45, 80, 139, 8080]

print(cs("\nTarget: ", "white").bold() + cs(target, "red").bold())

pstring = ""
for port in ports:
    pstring += str(port) + ","
print(cs("Ports: ", "white").bold() + cs(pstring[:-1:], "red").bold())

scanner = nmap.PortScanner()

# print the main info about each port and check if the host is up or down
for port in ports:
    scan = scanner.scan(target, pstring[:-1:], "-sC")
    print(f"\n\n-Port {port} is {scan['scan'][target]['tcp'][port]['state']}")  # state
    print(
        f" Service '{scan['scan'][target]['tcp'][port]['name']}' is running"
    )  # service name
    try:
        print(f" {scan['scan'][target]['tcp'][port]['script']}")  # basic script
    except KeyError:
        print(f" No script")

print(f"\n\nHost {target} is {scan['scan'][target]['status']['state']}\n")
