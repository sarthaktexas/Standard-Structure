# Contributing

## Adding a New Structure to an Existing Language or Framework

1. Create a directory under the framework/language directory with the name of the new structure, and add the necessary filesand directories to that newly created structure directory.
2. Use the CLI generation tool to generate a new structure by running `cd struct-add && pip3 install -r requirements.txt && python3 struct-add`. This will automatically generate a `README.md` for your new structure and create a directory tree for it.
3. Update the generated `README.md` file for the new structure directory so that necessary directories and files have explanations.