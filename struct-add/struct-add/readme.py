import os


def initializeMain():
    '''Initialize the main README.md for either language or framework
    '''
    formal_name = input(
        "\n What is the formal name (put in main project README)?:")
    template = '''
# {}

| 🏗️ Structure Name | 📚 Description |
|-------------------|----------------|
<!--END OF TOC, DO NOT REMOVE-->
'''.format(formal_name)
    with open('../README.md', 'w') as readme:
        readme.write(template)


def initialize(structure_name, tree, folders):
    '''Initialize the struct.md file

    Arguments:
        structure_name {str} -- Name of the structure
        tree {str} -- File tree
        folders {list} -- all the folders in the file tree
    '''
    template = '''
# {}

```
{}
```
'''
    for folder in folders:
        template = template + \
            '\n\n#`{}`\n\nA short description of what is in this folder'.format(
                folder)
    with open('./struct.md', 'w') as struct:
        struct.write(template)


def add_to_toc(structure_name):
    '''Add new structure to table of contents

    Arguments:
        structure_name {str} -- name of the new structure
    '''
    with open('../README.md') as readme:
        lines = readme.readlines()
    for i in range(len(lines)):
        if lines[i].strip() == '<!--END OF TOC, DO NOT REMOVE-->':
            lines.insert(i - 1, '  - [{n}](#{n})'.format(n=structure_name))
