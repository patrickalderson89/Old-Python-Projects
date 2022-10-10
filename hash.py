#!/usr/bin/python3

import hashlib
from sys import argv


def Hash(argv, htype):

    string = ""
    hashed = ""
    encode = "UTF-8"

    if argv[2] != "-f" and argv[2] != "--file":

        string = argv[2]

        if htype == "sha256":
            hashed = hashlib.sha256(bytes(string, encoding=encode)).hexdigest()
            print(f'\n"{string}" hashed: \n{hashed}\n\n')

        elif htype == "sha512":
            hashed = hashlib.sha512(bytes(string, encoding=encode)).hexdigest()
            print(f'\n"{string}" hashed: \n{hashed}\n\n')

        elif htype == "md5":
            hashed = hashlib.md5(bytes(string, encoding=encode)).hexdigest()
            print(f'\n"{string}" hashed: \n{hashed}\n\n')

    elif argv[2] == "-f" or argv[2] == "--file":

        file = argv[3]

        with open(file, "r") as f:
            destination = open(argv[4], "w")
            destination.write(f"Source: {argv[3]}, type: {argv[1]}\n\n")
            for word in f:
                word = word.rstrip()
                if htype == "sha256":
                    hashed = hashlib.sha256(bytes(word, encoding=encode)).hexdigest()
                elif htype == "sha512":
                    hashed = hashlib.sha512(bytes(word, encoding=encode)).hexdigest()
                elif htype == "md5":
                    hashed = hashlib.md5(bytes(word, encoding=encode)).hexdigest()

                destination.write(f"{word}: {hashed}\n\n")

        print("\nFile saved correctly\n\n")
        destination.close()

if __name__ == "__main__":

    help_msg = "\nSyntax: [file] [hash_type] [word or file] [destination file]\n\n"

    try:
        hash_type = argv[1][2:]
        Hash(argv, hash_type)

    except SyntaxError:
        print(help_msg)

    except ValueError:
        print(help_msg)

    except IndexError:
        print(help_msg)
