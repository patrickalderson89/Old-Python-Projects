#!/usr/bin/python3

import hashlib
from sys import argv


def Crack(argv, htype):

    crack_file = "/home/patrickalderson/Documents/rockyou.txt"

    if argv[2] == "-f" or argv[2] == "--file":
        source = open(argv[3], "r")
        destination = open(argv[4], "w")
        destination.write(f"Source: '{argv[3]}', type: '{htype}'\n\n")
        with open(crack_file, "r", encoding="ISO-8859-1") as f:
            for Hash in source:
                Hash = Hash.rstrip().lower()
                for passwd in f:
                    passwd = passwd.rstrip()
                    passwd_hashed = ""
                    found = False
                    if htype == "sha256":
                        passwd_hashed = hashlib.sha256(passwd.encode()).hexdigest()
                    elif htype == "sha512":
                        passwd_hashed = hashlib.sha512(passwd.encode()).hexdigest()
                    elif htype == "md5":
                        passwd_hashed = hashlib.md5(passwd.encode()).hexdigest()

                    if Hash == passwd_hashed:
                        found = True
                        break

                if found:
                    destination.write(f"Hash: {Hash}\nString: {passwd}\n\n\n")
                else:
                    destination.write(f"Hash: {Hash}\nString: Not Found\n\n\n")                 


        source.close()
        destination.close()


    else:
        Hash = argv[2]
        with open(crack_file, "r", encoding="ISO-8859-1") as f:
            for passwd in f:
                passwd = passwd.rstrip()
                
                if htype == "sha256":
                    passwd_hashed = hashlib.sha256(passwd.encode()).hexdigest()
                elif htype == "sha512":
                    passwd_hashed = hashlib.sha512(passwd.encode()).hexdigest()
                elif htype == "md5":
                    passwd_hashed = hashlib.md5(passwd.encode()).hexdigest()
                
                if Hash.lower() == passwd_hashed:
                    found = True
                    break
        if found:
            print(f"\nFound: '{passwd}'!\n\n")
        else:
            print("\nNot found.\n\n")
        


if __name__ == "__main__":

    help_msg = "\nSyntax: [file] [hash_type] [word or file] [destination file]\n\n"

    try:
        hash_type = argv[1][2:]
        Crack(argv, hash_type)

    except SyntaxError:
        print(help_msg)

    except ValueError:
        print(help_msg)

    except IndexError:
        print(help_msg)

    else:
        if argv[2] == "--file" or argv[2] == "-f":
            print("\n\t***** File saved correctly *****\n\n")
