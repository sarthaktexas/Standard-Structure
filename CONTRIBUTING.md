# How to Contribute

Hello! Thank you so much for showing interest in Standard-Structure. Below is the process you should take if you want to contribute.

## Before you start

1. Make sure the file structure you are planning on adding isn't already part of the project.

## Adding a new framework or language

To add a framework or language that isn't already part of Standard-Structure do the following:

1. Make the folder with the name of the framework or language under either `/frameworks` or `/languages`.
2. Inside of that folder make a `README.md` and a `examples` directory.

### `README.md`

The inside of the README.md is where most of the information is located. There is a `##` for each type of application. The first application type you should add is a basic application. The application should include a file tree with the layout of the folders and files wrapped in ```. Use the characters `┏`, `┃`, and `┗` to make the file tree and two spaces for indentation. Below is an example:

```
┏bin
┃ ┗main.dart
┃
┣lib
┃ ┗basic.dart
┃
┗test
  ┗basic_test.dart
```

Once you've added the file tree add a `###` with the folder name for each folder. Inside add a description of the folder describing its purpose in the scope of the project.

### Example `README.md`

````md
# 🎯 Dart

## Basic

[Example Application](examples/basic/)
​​​​```
┏bin
┃ ┗main.dart
┃
┣lib
┃ ┗basic.dart
┃
┗test
  ┗basic_test.dart

​​​​```

### `bin`

`bin` really only holds `main.dart` which is the entry point to the program

### `lib`

`lib` is where most of the code for a dart project goes.

### `test`

`test` holds all the unit tests for the project.
````

### Actual Example

In the `examples` directory you created before add an actual basic project and link to it in your `README.md` above the file tree as seen in the example `README.md` above
