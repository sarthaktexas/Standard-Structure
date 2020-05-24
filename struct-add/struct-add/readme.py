import os


def initialize():
    '''Initialize the README.md file
    '''
    formal_name = input(
        '\n What is the formal name (put in main project README)?:')
    template = '''
# {}


<!--END OF TOC, DO NOT REMOVE-->
'''.format(formal_name)
    with open('../README.md', 'w') as readme:
        readme.write(template)


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
