#!/usr/bin/env python3


'''
    FEEL FREE TO MAKE THIS CODE BETTER
'''
import os
from cryptography.fernet import Fernet
from colorama import Fore, Back, Style
import shutil
import sys

def encrypt_file(file_name,key):
    f = Fernet(key)
    try:
        with open(file_name,"rb") as fil:
            file_data = fil.read()
            encrypted_data = f.encrypt(file_data)
            with open(file_name, "wb") as fil:
                fil.write(encrypted_data)
    except:
        print(f'[IGNORING]{file_name}')

def main():
    if os.path.exists('secret.key'):
        print(Fore.RED+'[FOUND A SECRET KEY]'+Style.RESET_ALL)
        ch = input("Secret Key Found ! Do you want to remove it?(Y)")
        if ch == 'Y' or ch =='y':
            os.remove("secret.key")
        else:
            sys.exit("Aborting!")
    global allf
    allf = list(os.walk('.'))
    global folders
    folders = allf[0][1]
    print("[ZIPPING ALL THE FOLDERS]")
    for folder in folders:
        print(Fore.RED+f"[ZIPPING FOLDER] {folder}"+Style.RESET_ALL)
        shutil.make_archive(folder, 'zip',folder)
        shutil.rmtree(folder)
        print(Fore.GREEN+f"[ZIPPING DONE] {folder}"+Style.RESET_ALL)

    allf = list(os.walk('.'))
    global files
    files = allf[0][2]
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        key_file.close()
    print(Fore.GREEN+"[SECRET KEY IS EXPORTED TO secret.key]\n"+Style.RESET_ALL)
    print(Fore.RED+"[ENCRYPTION IN PROCESS] [FILES]")
    print(Style.RESET_ALL)
    for fil in files:
        print(Fore.RED+f'PROCESSING {fil}'+Style.RESET_ALL)
        encrypt_file(fil,key)
        print(Fore.GREEN+f'COMPLETED {fil}'+Style.RESET_ALL)
    print(Fore.GREEN+"\n[ENCRYPTION COMPLETE] [FILES]"+Style.RESET_ALL)
    ch = input("Do you want to remove the secret.key?(Y)")
    if ch == 'Y' or ch =='y':
        os.remove("secret.key")
    else:
        sys.exit(Fore.CYAN+f'[ALL DONE !!!]'+Style.RESET_ALL)
    print(Fore.CYAN+f'[ALL DONE !!!]'+Style.RESET_ALL)



if __name__ == "__main__":
    main()
