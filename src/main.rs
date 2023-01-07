mod encryption;
mod core;
mod models;
mod utils;

use clap::Command;

fn main() -> Result<(),Box<dyn std::error::Error>> {
    let matches = clap::Command::new("wdcrypt")
        .version("2.1.0")
        .author("Stefin stefin@pm.me")
        .about("Encrypt your current working directory")
        .arg_required_else_help(true)
        .subcommand(
            Command::new("encrypt")
                .short_flag('e')
                .long_flag("encrypt")
                .about("Encrypt the current working directory"),
        )
        .subcommand(
            Command::new("decrypt")
                .short_flag('d')
                .long_flag("decrypt")
                .about("Decrypt the current working directory"),
        )
        .get_matches();
    match matches.subcommand() {
        Some(("encrypt", _sub_matches)) => {
            let encryption_key =
                encryption::write_fernet_key_to_file(fernet::Fernet::generate_key());
            core::tar_all_dirs()?;
            core::encrypt_all_files(encryption_key)?;
        }
        Some(("decrypt", _sub_matches)) => {
            let encryption_key = encryption::read_fernet_key_from_file();
            core::decrypt_all_files(encryption_key)?;
            core::untar_all_dirs()?;
        }
        _ => {}
    }
    Ok(())
}
