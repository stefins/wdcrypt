use crate::core;

pub struct File<'a> {
    name: &'a str,
    fernet_key: &'a str,
}

impl<'a> File<'a> {
    pub fn new(name: &'a str, fernet_key: &'a str) -> Self {
        Self { name, fernet_key }
    }
    pub fn encrypt(&self) -> Result<(), Box<dyn std::error::Error>> {
        core::encrypt_file(self.name, self.fernet_key)
    }

    pub fn decrypt(&self) -> Result<(), Box<dyn std::error::Error>> {
        core::decrypt_file(self.name, self.fernet_key)
    }
}

impl Drop for File<'_> {
    fn drop(&mut self) {}
}

#[cfg(not(target_arch = "wasm32"))]
pub struct Folder<'a> {
    name: &'a str,
}

#[cfg(not(target_arch = "wasm32"))]
impl<'a> Folder<'a> {
    pub fn new(name: &'a str) -> Self {
        Self { name }
    }
    pub fn tar(&self) -> Result<(), Box<dyn std::error::Error>> {
        core::create_tar_gz(self.name)
    }
    pub fn untar(&self) -> Result<(), Box<dyn std::error::Error>> {
        core::untar_dir(self.name)
    }
}
