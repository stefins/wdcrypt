# wdcrypt-rs
[![Rust](https://github.com/stefins/wdcrypt-rs/actions/workflows/rust.yml/badge.svg)](https://github.com/stefins/wdcrypt-rs/actions/workflows/rust.yml)

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
Stefin stefin@pm.me
Encrypt your current working directory

USAGE:
    wdcrypt [OPTIONS]

OPTIONS:
    -d, --decrypt    Decrypt the current working directory with key
    -e, --encrypt    Encrypt the current working directory
    -h, --help       Print help information
    -V, --version    Print version information
```

## License 
MIT
