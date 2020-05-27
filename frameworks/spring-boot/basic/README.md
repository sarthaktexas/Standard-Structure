![Spring Boot](https://img.shields.io/static/v1?label=Framework&message=Spring%20Boot&color=6DB33F&logo=spring&logoColor=white&style=for-the-badge)

## Minimal Application Template

```
├── src/
│   ├── test/
│   └── main/
│       ├── java/
│       │   └── com/
│       │       └── <user/org>/
│       │           └── <artifact>/
│       │               ├── controller
│       │               │   └── MainController.java
│       │               ├── dao/
│       │               └── Application.java
│       └── resources/
│           ├── static/
│           ├── templates/
│           └── application.properties
├── mvnw/
│   └── mvnw.cmd
└── pom.xml
```

### `Application.java`

Specifies what to do when the application runs.

### `controller`

Contains controller classes.

### `dao`

The Data Access Object folder is only if you have databases in your application.

### `java/com/<user/org>/<artifact>`

These are automatically generated usually empty directories.  It is standard practice to let these be.  

### `MainController.java`

The file for your main controller.

### `mvnw/mvnw.cmd`

These are files automatically generated when creating a maven project.  They ensure that that a maven project can be run without maven being installed on the machine.

### `pom.xml`

This file contains information about all of the dependencies and the versions of each.  This is usually automatically generated when you create a maven project.

### `static`

Contains static assets.

### `src`

Contains the code to your application.

### `templates`

Contains templets for pages, usually html pages.

### `test`

Contains tests for your application.
