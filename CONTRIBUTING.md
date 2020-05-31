# How to Contribute

Hello! Thank you so much for showing interest in Standard-Structure!

## What defines a structure? (Vocabulary)

Regardless of what anyone else on the Internet says, or what you believe, we, the creators and maintainers of Standard-Structure, define a structure as:
> A bare-bones template for a use case for a language or framework that includes all necessary files for development using that use case. This does not extend to minutiae changes, and is more applicable to, for example, the use of Golang for a CLI (one structure) or a web application (another structure).

A language is defined as a programming language. The following are considered programming languages:
- Python
- TypeScript
- Julia
- Golang
- Clojure
- Java

A framework is defined as an extension of the functionality of a programming language for a specific application. The following are considered frameworks:
- React.js
- AngularJS
- AngularDart
- Flask
- Django
- Deno
- Spring Boot

## Before you start

1. Make sure the file structure you are planning on adding isn't already:
  - Part of the project
  - Part of a PR waiting to be merged

## Learn by example

This document is meant to be an in-depth description of what a language/framework looks like in the Standard-Structure project. However, you'll likely find it easier to look at the existing languages/frameworks, and follow their example.

## The anatomy of the Standard-Structure project

There are two root directories, `frameworks/` and `languages/`. `languages/` is for **programming languages**, and `frameworks` is for **everything else**. Both share an identical structure, containing a subdirectory for each language or framework.

Each language/framework directory contains at least two items, a `README.md` (that acts as a table of contents), and a directory for each **structure**. Every language/framework contains at least one **structure**, with `basic/` being the required default. A

Each structure needs to have a `README.md` that describes the structure.

#### Here's what a directory tree looks like:
```
├── frameworks/
│   └── react/
│       ├── README.md
│       ├── basic/
│       │   ├── README.md
│       │   └── YOUR STRUCTURE GOES HERE
│       └── another_structure/
│           ├── README.md
│           └── YOUR STRUCTURE GOES HERE
└── languages/
    └── python/
        ├── README.md
        └── basic/
            ├── README.md
            └── YOUR STRUCTURE GOES HERE
```

## Adding a new framework or language

To add the structure for a framework or language that isn't already part of this project, or add a new framework or language, do the following:

1. Make a directory with the name of that framework or language under `/frameworks` or `/languages`, respectively.
2. Create a `basic/` directory under the framework/language directory, and add the structure for a basic project using that language/framework to that `basic/` directory.
3. Use the CLI generation tool to generate a new structure by running `cd struct-add && pip3 install -r requirements.txt && python3 struct-add`. This will automatically generate a `README.md` for your new framework/language and its `basic/` project and create a directory tree for it.
4. Update the generated `README.md` file for the `basic/` directory so that necessary directories and files have explanations.

## Adding a new structure to an existing framework or language

1. Create a directory under the framework/language directory with the name of the new structure, and add the necessary filesand directories to that newly created structure directory.
2. Use the CLI generation tool to generate a new structure by running `cd struct-add && pip3 install -r requirements.txt && python3 struct-add`. This will automatically generate a `README.md` for your new structure and create a directory tree for it.
3. Update the generated `README.md` file for the new structure directory so that necessary directories and files have explanations.

#### Example:

##### Main README.md:
```md
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

| Structure               | Description                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------- |
| [Basic Vue App](basic/) | A starting point for a Vue app without Vuex or Vue Router generated with the Vue CLI. |
<!--END OF TOC, DO NOT REMOVE-->
```
##### Rendered:
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

| Structure                              | Description                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------- |
| [Basic Vue App](frameworks/vue/basic/) | A starting point for a Vue app without Vuex or Vue Router generated with the Vue CLI. |
<!--END OF TOC, DO NOT REMOVE-->

##### `basic/README.md`

The inside of the README.md is where most of the information is located. For each critical file or directory (a tests directory, the entry point of the application, etc.), explain the function and purpose of that file or directory.

For the basic Dart App, for example, this is the `README.md`:


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


# Footnotes
## Badges
Want a fancy badge like this?
<br>
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

We use shields.io to generate badges for languages and frameworks.