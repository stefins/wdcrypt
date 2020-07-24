#!/usr/bin/env python3

import argparse
from wdcrypt import decrypt
from wdcrypt import encrypt
__author__ = "Stef"

def main():
    my_parser = argparse.ArgumentParser(description='Encrypt and decrypt your current working directory')
    my_parser.add_argument('-e','--encrypt', action='store_true',help='Encrypt all files and folders')
    my_parser.add_argument('-d','--decrypt', action='store_true',help='Decrypt all files and folders')
    args = my_parser.parse_args()
    if (vars(args)['encrypt']):
        encrypt.main()
    elif (vars(args)['decrypt']):
        decrypt.main()
    else:
        my_parser.print_help()

if __name__ == '__main__':
    main()
