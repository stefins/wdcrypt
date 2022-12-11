use std::{
    io::{self, BufRead, Write},
    path::Path,
};

/// Wait for user input and return what they typed
fn read_line() -> Option<String> {
    let stdin = io::stdin();
    let stdin = stdin.lock();
    let mut lines = stdin.lines();
    lines.next().and_then(|l| l.ok())
}

/// Ask a yes/no question to the user
pub fn ask_bool(question: &str, default: bool) -> Option<bool> {
    let stdout = io::stdout();
    let mut stdout = stdout.lock();
    write!(
        &mut stdout,
        "{} {}: ",
        question,
        if default { "[Y/n]" } else { "[y/N]" }
    )
    .unwrap();
    stdout.flush().unwrap();
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

// This fn returns true if the file is to be overwritten
pub fn warn_if_file_exists(name: &str) -> bool {
    if Path::new(name).exists() {
        return ask_bool(&format!("File {} already exists! Overwrite?", name), true).unwrap();
    }
    true
}
