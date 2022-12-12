mod encryption;
mod file_utils;
mod models;
mod utils;

use clap::Command;

fn main() -> Result<(),Box<dyn std::error::Error>> {
    let matches = clap::Command::new("wdcrypt")
        .version("2.0.1")
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
            file_utils::tar_all_dirs()?;
            file_utils::encrypt_all_files(encryption_key)?;
        }
        Some(("decrypt", _sub_matches)) => {
            let encryption_key = encryption::read_fernet_key_from_file();
            file_utils::decrypt_all_files(encryption_key)?;
            file_utils::untar_all_dirs()?;
        }
        _ => {}
    }
    Ok(())
}
