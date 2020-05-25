from pathlib import Path
import os


def initializeMain():
    '''Initialize the main README.md for either language or framework
    '''
    formal_name = input(
        "\nWhat is the formal name (put in main project README, e.g. 🎯 [Dart](https://dart.dev/))?:\n\n")
    template = f'''# {formal_name}

| 🏗️ Structure Name | 📚 Description |
|-------------------|----------------|
<!--END OF TOC, DO NOT REMOVE-->
'''
    with open('../README.md', 'w') as readme:
        readme.write(template)


def initialize(structure_name, tree):
    '''Initialize the struct.md file

    Arguments:
        structure_name {str} -- Name of the structure
        tree {str} -- File tree
        folders {list} -- all the folders in the file tree
    '''
    template = f'''# {structure_name}

```
{tree}
```
'''
    with open('./README.md', 'w') as struct:
        struct.write(template.format(structure_name, tree))


def add_to_toc(structure_name):
    '''Add new structure to table of contents

    Arguments:
        structure_name {str} -- name of the new structure
    '''
    with open('../README.md') as readme:
        lines = list(readme.readlines())
    description = input(
        '\nWhat is the description of the structure you are adding (1 - 2 sentences)?:\n\n')
    updated_lines = []
    for line in lines:
        if line.strip() == '<!--END OF TOC, DO NOT REMOVE-->':
            updated_lines.append(
                f'| [{structure_name}](./{structure_name}) | {description} |\n')
        updated_lines.append(line)
    with open('../README.md', 'w') as readme:
        readme.writelines(updated_lines)


def tree(dir_path: Path, prefix: str = ''):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters

    Gotten from https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
    Thank you Aaron Hall!

    """
    # prefix components:
    space = '    '
    branch = '│   '
    # pointers:
    tee = '├── '
    last = '└── '
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir():  # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)
