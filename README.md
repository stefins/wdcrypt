![Upload Python Package](https://github.com/IamStefin/wdcrypt/workflows/Upload%20Python%20Package/badge.svg)

# wdcrypt
A Python package to encrypt your working directory with a terminal command. This package will use Fernet. Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.<br/>
Find more about Fernet [here.](https://cryptography.io/en/latest/fernet/)<br/><br/>
Note:IF YOU LOSE THE `secret.key` FILE IT WILL BE IMPOSSIBLE TO GET BACK YOUR FILES.
# Installation
```console
$ pip install wdcrypt

---> 100%
```

# Usage

```console
$ wdcrypt
usage: wdcrypt [-h] [-e] [-d]

Encrypt and decrypt your current working directory

optional arguments:
  -h, --help     show this help message and exit
  -e, --encrypt  Encrypt all files and folders
  -d, --decrypt  Decrypt all files and folders
```

# Contributions
Contributions are always welcome!

# License
MIT License
