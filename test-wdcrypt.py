#!/usr/bin/python3

import os
import shutil
import subprocess
from random import randbytes

TEMP_DIR_1 = "/tmp/wdcrypt/1/"
TEMP_DIR_2 = "/tmp/wdcrypt/2/"

SECRET_KEY = ".secret.key"


class TestWdcryptFileOnly:
    sha256dict = {}

    def __init__(self):
        os.makedirs(TEMP_DIR_1, exist_ok=True)
        os.chdir(TEMP_DIR_1)
        for n in range(10):
            file_name = TEMP_DIR_1 + "file-" + str(n)
            self.sha256dict[file_name] = new_file_return_hash(file_name)

    def run(self):
        if os.system("wdcrypt -e >/dev/null 2>&1") != 0:
            raise Exception("Wdcrypt -> non zero exit code")
        if os.system("wdcrypt -d >/dev/null 2>&1") != 0:
            raise Exception("Wdcrypt -> non zero exit code")
        for n in range(10):
            file_name = TEMP_DIR_1 + "file-" + str(n)
            if self.sha256dict[file_name] != get_hash_of_file(file_name):
                raise Exception("Hash mismatch!")
        print("[PASSED] TestWdcryptFileOnly")

    def __del__(self):
        for n in range(10):
            file_name = TEMP_DIR_1 + "file-" + str(n)
            os.remove(file_name)
        os.remove(SECRET_KEY)
        shutil.rmtree(TEMP_DIR_1)


class TestWdcryptFileAndDir:
    sha256dict = {}

    def __init__(self):
        os.makedirs(TEMP_DIR_2, exist_ok=True)
        os.chdir(TEMP_DIR_2)
        for dn in range(10):
            dir_name = TEMP_DIR_2 + "dir-" + str(dn) + "/"
            os.mkdir(dir_name)
            for n in range(10):
                file_name = dir_name + "file-" + str(n)
                self.sha256dict[file_name] = new_file_return_hash(file_name)

    def run(self):
        if os.system("wdcrypt -e >/dev/null 2>&1") != 0:
            raise Exception("Wdcrypt -> non zero exit code")
        if os.system("wdcrypt -d >/dev/null 2>&1") != 0:
            raise Exception("Wdcrypt -> non zero exit code")
        for dn in range(10):
            dir_name = TEMP_DIR_2 + "dir-" + str(dn) + "/"
            for n in range(10):
                file_name = dir_name + "file-" + str(n)
                if self.sha256dict[file_name] != get_hash_of_file(file_name):
                    raise Exception("Hash mismatch!")
        print("[PASSED] TestWdcryptFileAndDir")

    def __del__(self):
        for dn in range(10):
            dir_name = TEMP_DIR_2 + "dir-" + str(dn) + "/"
            shutil.rmtree(dir_name)
        os.remove(SECRET_KEY)
        shutil.rmtree(TEMP_DIR_2)


def new_file_return_hash(file_name):
    with open(file_name, "wb") as file:
        num_chars = 1024 * 1024 * 5
        file.write(randbytes(num_chars))
        return subprocess.check_output(["sha256sum", file.name]).decode("utf-8")[0:64]


def get_hash_of_file(file_name):
    return subprocess.check_output(["sha256sum", file_name]).decode("utf-8")[0:64]


def installCurrentWdcrypt():
    return os.system("cargo install --path . >/dev/null 2>&1")


def main():
    if installCurrentWdcrypt() != 0:
        raise Exception("Cannot install wdcrypt...")
    TestWdcryptFileOnly().run()
    TestWdcryptFileAndDir().run()


if __name__ == "__main__":
    main()
