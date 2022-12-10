use std::io::{self, BufRead, Write};

/// Wait for user input and return what they typed
fn read_line() -> Option<String> {
    let stdin = io::stdin();
    let stdin = stdin.lock();
    let mut lines = stdin.lines();
    lines.next().and_then(|l| l.ok())
}

/// Ask a yes/no question to the user
pub fn ask_bool(question: &str, default: bool) -> Option<bool> {
    print!("{} {}: ", question, if default { "[Y/n]" } else { "[y/N]" });
    let _ = io::stdout().flush();
    let input = read_line().unwrap();

    match &*input {
        "y" | "Y" | "yes" | "YES" | "true" => Some(true),
        "n" | "N" | "no" | "NO" | "false" => Some(false),
        "" => Some(default),
        _ => {
            println!("Invalid choice: '{}'", input);
            ask_bool(question, default)
        }
    }
}

/*
match ask_bool("Do you want to use the existing key?", false).unwrap(){
            true => {},
            false => {
                process::exit(1);
            }
        }
*/
