# Contributing

## Adding a New Language or Framework

To add the structure for a framework or language that isn't already part of this project, or add a new framework or language, do the following:

1. Make a directory with the name of that framework or language under `/frameworks` or `/languages`, respectively.
2. Create a `basic/` directory under the framework/language directory, and add the structure for a basic project using that language/framework to that `basic/` directory.
3. Use the CLI generation tool to generate a new structure by running `cd struct-add && pip3 install -r requirements.txt && python3 struct-add`. This will automatically generate a `README.md` for your new framework/language and its `basic/` project and create a directory tree for it.
4. Update the generated `README.md` file for the `basic/` directory so that necessary directories and files have explanations.
5. Add the badge for your language or framework to the Standard-Structure repository `README.md` under the appropriate section. Replace the top-level header in the framework/language `README.md` with the generated badge.

## Language and Framework Badges

This is an example badge for the Vue framework:

![Vue](https://img.shields.io/static/v1?label=Framework&message=Vue&color=4FC08D&logo=vue.js&logoColor=white&style=for-the-badge)

You should use shields.io to generate badges for your languages or frameworks. In the unlikely event that your language or framework cannot be generated from shields.io, please discuss it in your pull request.