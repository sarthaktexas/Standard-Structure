![Rust](http://img.shields.io/static/v1?label=Language&message=Rust&color=black&logo=rust&logoColor=white&style=for-the-badge)
## Minimal Template

```
├── src/
│   └── main.rs
└── Cargo.toml
```

### `src/`

`src/` is just the folder that holds all your source files.

### `src/main.rs`

This is the main file that `cargo` will use for `cargo build` and `cargo run`. It should be relatively small, and only contain the code that you absolutely need for running the program.

### `Cargo.toml`

This is the file that `cargo` uses for dependency management, `crates.io` metadata, and just general information about your project.

### `Cargo.lock`

When `cargo` installs dependencies, it checks for the latest version of them that will work with your project and generates a `Cargo.lock` file with all the current versions of each of the dependencies. This file does not change manually, and it ensures that all installations of your project will work better.
