# How to Contribute

Hello! Thank you so much for showing interest in Standard-Structure.

## Before you start

1. Make sure the file structure you are planning on adding isn't already:
  - Part of the project
  - Part of a PR waiting to be merged

## Learn by example

This doc is meant to be an in-depth description of what a language/framework looks like in the Standard-Structure project. However, you'll likely find it easier to look at the existing languages/frameworks, and follow their example.

## The anatomy of the Standard-Structure project

There are two root directories, `frameworks/` and `languages/`. `languages/` is for **programming languages**, and `frameworks` is for **everything else**. Both share an identical structure, containing a subdirectory for each language or framework.

I'll be referring to languages/frameworks as **languages**, but I really mean both languages and frameworks.

Each language directory contains at least two items, a `README.md` (that acts as a table of contents), and a directory for each **structure**. Every language contains at least one **structure**, with `basic/` being the required default. A

Each structure needs to have a `README.md` that describes the structure.

#### Here's what our repo looks like:
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

## Adding a new framework or language project structure

To add the structure for framework or language that isn't already part of this project, do the following:

1. Make a directory with the name of that framework or language under `/frameworks` or `/languages`, respectively.
2. Inside of that directory create a `README.md`. In this file, put your **[framework/language badge](#badges)** and a **table of contents**.

#### Example:
```md
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

| Structure | Description |
|-----------|-------------|
| [Basic Vue App](basic/) | A starting point for a Vue app without Vuex or Vue Router generated with the Vue CLI. |
<!--END OF TOC, DO NOT REMOVE-->
```
#### Rendered:
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

| Structure | Description |
|-----------|-------------|
| [Basic Vue App](frameworks/vue/basic/) | A starting point for a Vue app without Vuex or Vue Router generated with the Vue CLI. |
<!--END OF TOC, DO NOT REMOVE-->

### `README.md`

The inside of the README.md is where most of the information is located. There is a `##` for each type of application. The first application type you should add is a basic application. The application should include a file tree with the layout of the folders and files wrapped in ```. Use the characters `├`, `│`, `─` and `└` to make the file tree and two spaces for indentation. Below is an example:

```
├── bin/
│   └── main.dart
│
├── lib/
│   └── basic.dart
│
└── test/
    └── basic_test.dart
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

`bin` really only holds `main.dart` which is the entry point to the program

### `lib`

`lib` is where most of the code for a dart project goes.

### `test`

`test` holds all the unit tests for the project.
````


# Footnotes
## Badges
Want a fancy badge like this? ![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

We use shields.io to generate badges for languages and frameworks