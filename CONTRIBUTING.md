# How to Contribute

Hello! Thank you so much for showing interest in Standard-Structure!

## Vocabulary

Regardless of what anyone else on the Internet says, or what you believe, we, the creators and maintainers of Standard-Structure, define the following vocabulary for use within this project:

| Word      | Definition                                                                                                                                                                                                                                                                                                                                   | Examples                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Structure | A bare-bones file structure for a use case of a language or framework that includes all necessary files for development of an application of that use case. This does not extend to minutiae changes such as the addition of a single prebuilt component to a React App, but does extend to the use of React Router with React, for example. | The use of Golang for a CLI is one structure, while the use of Golang for a web app is another structure      |
| Language  | A programming language.                                                                                                                                                                                                                                                                                                                      | <ul><li>Python</li><li>TypeScript</li><li>Julia</li><li>Golang</li><li>Clojure</li><li>Java</li></ul>         |
| Framework | A platform for developing software applications that provides a foundation of functionality that can be extended for application-specific use.                                                                                                                                                                                               | <ul><li>React.js</li><li>Next.js</li><li>AngularDart</li><li>Flask</li><li>Deno</li><li>Spring Boot</li></ul> |

## Before you start

<ul>
  <li>Make sure the structure, language, or framework you are planning on adding isn't already:
    <ul>
      <li>Part of the project</li>
      <li>Part of a pull request waiting to be merged</li>
    </ul>
  </li>
</ul> 

## Learn by example

This document is meant to provide you with the necessary resources to add new structures, languages, or frameworks to the project. However, the best thing you could do before reading farther in this document is to go check out some of the [languages](./languages/), [frameworks](./frameworks/), and structures within those languages and frameworks to get a sense for what the project structure and style looks like.

## The anatomy of the Standard-Structure project

There are two root directories, `frameworks/` and `languages/`. `languages/` is for languages, and `frameworks` is for frameworks. Each contain subdirectories for each language or framework, respectively.

Each language/framework directory contains at least two items, a `README.md` (that acts as a table of contents), and a directory for each **structure**. Every language/framework contains at least one **structure**, with `basic/` being the required default.

Every structure needs to have a `README.md` that describes the structure.

#### This is what part of the directory tree for Standard-Structure might look like:
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

## Adding a New Framework or Language

Please see [Adding a New Language or Framework](./docs/Adding%20a%20New%20Language%20or%20Framework.md) for details.

## Adding a New Structure to an Existing Framework or Language

Please see [Adding a New Structure](./docs/Adding%20a%20New%20Language%20or%20Framework.md) for details.

### Example:

#### Main README.md:
```md
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

| Structure               | Description                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------- |
| [Basic Vue App](basic/) | A starting point for a Vue app without Vuex or Vue Router, generated with the Vue CLI. |
<!--END OF TOC, DO NOT REMOVE-->
```
##### Rendered:
![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

| Structure                              | Description                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------- |
| [Basic Vue App](frameworks/vue/basic/) | A starting point for a Vue app without Vuex or Vue Router generated with the Vue CLI. |
<!--END OF TOC, DO NOT REMOVE-->

#### Structure README.md

The inside of the README.md for each structure is where most of the information is located. For each critical file or directory within that structure (a tests directory, the entry point of the application, etc.), explain the function and purpose of that file or directory.

For the basic Dart App, for example, this is the `README.md`:


````md
# ![Dart](http://img.shields.io/static/v1?label=&message=Dart&color=0175c2&logo=dart&logoColor=white&style=for-the-badge)

## Basic

[Example Application](examples/basic/)

```
├── bin/
│   └── main.dart
├── lib/
│   └── basic.dart
└── test/
    └── basic_test.dart
```

### `bin`

`bin` really only holds `main.dart` which is the entry point to the program

### `lib`

`lib` is where most of the code for a dart project goes.

### `test`

`test` holds all the unit tests for the project.
````

##### Rendered

# ![Dart](http://img.shields.io/static/v1?label=&message=Dart&color=0175c2&logo=dart&logoColor=white&style=for-the-badge)

## Basic

[Example Application](examples/basic/)

```
├── bin/
│   └── main.dart
├── lib/
│   └── basic.dart
└── test/
    └── basic_test.dart
```

### `bin`

`bin` really only holds `main.dart` which is the entry point to the program

### `lib`

`lib` is where most of the code for a dart project goes.

### `test`

`test` holds all the unit tests for the project.