mod encryption;
mod file_utils;
mod models;
mod utils;

use clap::Command;

fn main() {
    let matches = clap::Command::new("wdcrypt")
        .version("0.1.1")
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
            file_utils::tar_all_folders().unwrap();
            file_utils::encrypt_all_files().unwrap();
        }
        Some(("decrypt", _sub_matches)) => {
            file_utils::decrypt_all_files().unwrap();
        }
        _ => {}
    }
}
