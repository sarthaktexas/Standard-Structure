import os


def location():
    '''Get the location of structure

    Raises:
        Exception: Error if language or framework isn't chosen
        Exception: Error if the folder chosen doesn't exist

    Returns:
        str -- path of structure
    '''
    path = ''
    print(
        '''
👋 Hello! Thank you for contributing to Standard-Structure!
Below are some questions about the structure you are trying to add:
    '''
    )
    lang_or_frame = input('Is it a language or a framework? (l or f): ')
    if 'f' == lang_or_frame.lower():
        path = '../frameworks/'
    elif 'l' == lang_or_frame.lower():
        path = '../languages/'
    else:
        raise Exception(
            '{} is neither language or framework'.format(lang_or_frame))

    # Asking the user the name and
    lang_or_frame_name = input(
        'What is the name of the technology or framework in standard structure?: ')
    path = path + lang_or_frame_name + '/'
    if not os.path.exists(path):
        raise Exception("Looks like {} doesn't exist".format(path))

    return path
