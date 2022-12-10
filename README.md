# wdcrypt-rs
[![Rust](https://github.com/stefins/wdcrypt/actions/workflows/rust.yml/badge.svg)](https://github.com/stefins/wdcrypt/actions/workflows/rust.yml)
[![releaser](https://github.com/stefins/wdcrypt/actions/workflows/release.yml/badge.svg)](https://github.com/stefins/wdcrypt/actions/workflows/release.yml)

A Rust CLI to encrypt the current working directory with Fernet encryption.
Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.
<br/>
Find more about Fernet [here](https://cryptography.io/en/latest/fernet/)

## Installation
Make sure you have `cargo` in your $PATH
```bash
cargo install wdcrypt 
```

## Usage
```
Encrypt your current working directory

Usage: wdcrypt [COMMAND]

Commands:
  encrypt, -e, --encrypt  Encrypt the current working directory
  decrypt, -d, --decrypt  Decrypt the current working directory
  help                    Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help information
  -V, --version  Print version information
```

## License 
MIT
