import os

import ask
import readme


def main():
    '''Main function for the program
    '''
    location = ask.location()
    os.chdir(location)
    if not os.path.exists('../README.md'):
        # with open('../README.md')
    readme.add_to_toc(location.split('/')[-2])


if __name__ == '__main__':
    main()
