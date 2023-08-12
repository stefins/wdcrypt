#!/usr/bin/python3

import os
import shutil
from random import randbytes
import subprocess


TEMP_DIR = "/tmp/wdcrypt/"
SECRET_KEY = ".secret.key"


class TestWdcryptFileOnly:
    sha256dict = {}

    def __init__(self):
        try:
            shutil.rmtree(TEMP_DIR)
        except:
            pass
        os.mkdir(TEMP_DIR)
        os.chdir(TEMP_DIR)
        for n in range(10):
            file_name = TEMP_DIR+"file-"+str(n)
            self.sha256dict[file_name] = new_file_return_hash(file_name)

    def run(self):
        if os.system("wdcrypt -e >/dev/null 2>&1") != 0:
            raise Exception("Wdcrypt -> non zero exit code")
        if os.system("wdcrypt -d >/dev/null 2>&1") != 0:
            raise Exception("Wdcrypt -> non zero exit code")
        for n in range(10):
            file_name = TEMP_DIR+"file-"+str(n)
            if self.sha256dict[file_name] != get_hash_of_file(file_name):
                raise Exception("Hash mismatch!")
        print("[PASSED] TestWdcryptFileOnly")

    def __del__(self):
        for n in range(10):
            file_name = TEMP_DIR+"file-"+str(n)
            os.remove(file_name)
        os.remove(SECRET_KEY)


class TestWdcryptFileAndDir:
    def __init__(self):
        pass

    def run(self):
        pass

    def __del__(self):
        pass


def new_file_return_hash(file_name):
    with open(file_name, 'wb') as file:
        num_chars = 1024*1024*5
        file.write(randbytes(num_chars))
        return subprocess.check_output(['sha256sum', file.name]).decode('utf-8')[0:64]


def get_hash_of_file(file_name):
    return subprocess.check_output(['sha256sum', file_name]).decode('utf-8')[0:64]


def installCurrentWdcrypt():
    return os.system("cargo install --path . >/dev/null 2>&1")


def main():
    TestWdcryptFileOnly().run()
    TestWdcryptFileAndDir().run()


if __name__ == "__main__":
    if installCurrentWdcrypt() != 0:
        raise Exception("Cannot install wdcrypt...")
    main()
