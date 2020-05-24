import os


def initializeMain():
    '''Initialize the main README.md for either language or framework
    '''
    formal_name = input(
        "\nWhat is the formal name (put in main project README)?:\n\n")
    template = f'''# {formal_name}

| 🏗️ Structure Name | 📚 Description |
|-------------------|----------------|
<!--END OF TOC, DO NOT REMOVE-->
'''
    with open('../README.md', 'w') as readme:
        readme.write(template)


def initialize(structure_name, tree, folders):
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
    for folder in folders:
        template = template + \
            f'\n\n#`{folder}`\n\nA short description of what is in this folder'
    with open('./struct.md', 'w') as struct:
        struct.write(template.format(structure_name, tree))


def add_to_toc(structure_name):
    '''Add new structure to table of contents

    Arguments:
        structure_name {str} -- name of the new structure
    '''
    with open('../README.md') as readme:
        lines = list(readme.readlines())
    print(type(lines))
    description = input(
        '\nWhat is the description of the structure you are adding (1 - 2 sentences)?:\n\n')
    updated_lines = []
    for line in lines:
        if line.strip() == '<!--END OF TOC, DO NOT REMOVE-->' and f'| [{structure_name}](./{structure_name}) | {description} |\n' not in lines:
            updated_lines.append(
                f'| [{structure_name}](./{structure_name}) | {description} |\n')
        updated_lines.append(line)
    with open('../README.md', 'w') as readme:
        readme.writelines(updated_lines)
