use crate::file_utils;

pub struct File<'a> {
    name: &'a str,
    fernet_key: &'a str,
}

impl<'a> File<'a> {
    pub fn new(name: &'a str, fernet_key: &'a str) -> Self {
        Self { name, fernet_key }
    }
    pub fn encrypt(&self) -> Result<(), Box<dyn std::error::Error>> {
        file_utils::encrypt_file(self.name, self.fernet_key)
    }

    pub fn decrypt(&self) -> Result<(), Box<dyn std::error::Error>> {
        file_utils::decrypt_file(self.name, self.fernet_key)
    }
}

impl Drop for File<'_> {
    fn drop(&mut self) {}
}

pub struct Folder<'a> {
    name: &'a str,
}

impl<'a> Folder<'a> {
    pub fn new(name: &'a str) -> Self {
        Self { name }
    }
    pub fn tar(&self) -> Result<(), Box<dyn std::error::Error>> {
        file_utils::create_tar_gz(self.name)
    }
    fn untar(&self) -> Result<(), Box<dyn std::error::Error>> {
        file_utils::untar_dir(self.name)
    }
}
