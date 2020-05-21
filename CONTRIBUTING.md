# How to Contribute

Hello! Thank you so much for showing interest in Standard-Structure.

## Before you start

1. Make sure the file structure you are planning on adding isn't already:
  - Part of the project
  - Part of a PR waiting to be merged

## Adding a new framework or language project structure

To add the structure for framework or language that isn't already part of this project, do the following:

1. Make a directory with the name of that framework or language under `/frameworks` or `/languages`, respectively.
2. Inside of that directory create a `README.md` and an `examples` directory.

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

### `examples` directory

In the `examples` directory, create the structure described in your `README.md` and link to the example project above the file tree in your `README.md`.

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

bin really only holds `main.dart` which is the entry point to the program

### `lib`

lib is where most of the code for a dart project goes.

### `test`

test holds all the unit tests for the project.
````
