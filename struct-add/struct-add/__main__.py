import os
from pathlib import Path

import ask
import readme


def main():
    '''Main function for the program
    '''
    location = ask.location()
    os.chdir(location)
    if not os.path.exists('../README.md'):
        readme.initializeMain()
    readme.add_to_toc(location.split('/')[-2])
    treeCommand = readme.tree(Path.cwd())
    treeLines = []
    for line in treeCommand:
        treeLines.append(str(line))
    tree = '\n'.join(treeLines)
    readme.initialize(location.split('/')[-2], tree)


if __name__ == '__main__':
    main()
