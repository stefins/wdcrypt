#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
from colorama import Fore, Back, Style
import shutil
import sys


def decrypt_file(file_name):
    print(f"[DECRYPTING FILE] {file_name}")
    with open("secret.key","rb") as k:
        key = k.read()
    f = Fernet(key)
    if not(file_name=='secret.key'):
        try:
            with open(file_name,"rb") as fil:
                encrypted_data = fil.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(file_name,"wb") as fil:
                fil.write(decrypted_data)
        except:
            print(f'[IGNORING]{file_name}')
    else:
        print(f'[IGNORING]{file_name}')

def main():
    if os.path.exists('secret.key'):
        print(Fore.RED+'[FOUND A SECRET KEY]'+Style.RESET_ALL)
    else:
        sys.exit("SECRET KEY NOT FOUND! ABORTING")
    allf = list(os.walk('.'))
    files = allf[0][2]
    zip_files = []
    for fil in files:
        decrypt_file(fil)
        if fil.endswith('.zip'):
            zip_files.append(fil)
    print("[UNPACKING ZIP FILES]")
    for i in zip_files:
        print(Fore.RED+f"[UNZIPPING FILE] {i}"+Style.RESET_ALL)
        shutil.unpack_archive(i,i[:-4],'zip')
        os.remove(i)
        print(Fore.GREEN+f"[UNZIPPING DONE] {i}"+Style.RESET_ALL)
    print(Fore.CYAN+"[UNPACKING COMPLETED]"+Style.RESET_ALL)
    ch = input("Do you want to remove the secret.key?(Y)")
    if ch == 'Y' or ch =='y':
        os.remove("secret.key")
    else:
        sys.exit(Fore.CYAN+f'[ALL DONE !!!]'+Style.RESET_ALL)
    print(Fore.CYAN+f'[ALL DONE !!!]'+Style.RESET_ALL)

if __name__ == '__main__':
    main()
