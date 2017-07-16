"""Basic utility functions for ERP-SCANR."""

import os

################################################################################################
################################# ERPSC - UTILS - FUNCTIONS ####################################
################################################################################################

def erp_numbering(f_name):
    """Rewrites the number prefix in ERP term files.

    Parameters
    ----------
    f_name : str
        Full file path & name for file to run.
    """

    os.rename(f_name, 'temp.txt')

    with open('temp.txt', 'r') as old_file:
        with open(f_name, 'w') as new_file:

            for ind, line in enumerate(old_file):
                new_file.write('{:02}'.format(ind+1) + '-' + line[3:])

    os.remove('temp.txt')


def comb_terms(lst, jt):
    """Combine a list of terms to use as search arguments.

    Parameters
    ----------
    lst : list of str
        List of terms to combine together.
    jt : {'or', 'not'}
        Term to use to join together terms.

    Returns
    -------
    out : str
        String
    """

    # Add quotes to list items for exact search
    lst = ['"'+ item + '"' for item in lst]

    # Join together using requested join term
    if jt == 'or':
        out = '(' + 'OR'.join(lst) + ')'
    elif jt == 'not':
        out = 'NOT' + 'NOT'.join(lst)

    return out


def extract(dat, tag, how):
    """Extract data from HTML tag.

    Parameters
    ----------
    dat : bs4.element.Tag
        HTML data to pull specific tag out of.
    tag : str
        Label of the tag to extract.
    how : {'raw', 'all' , 'txt', 'str'}
        Method to extract the data.
            raw - extract an embedded tag
            all - extract all embedded tags
            txt - extract text as unicode
            str - extract text and convert to string

    Returns
    -------
    {bs4.element.Tag, bs4.element.ResultSet, unicode, str, None}
        Requested data from the tag. Returns None is requested tag is unavailable.
    """

    # Check how spec if valid
    if how not in ['raw', 'str', 'all']:
        raise ValueError('Value for how is not understood.')

    # Use try to be robust to missing tag
    try:
        if how is 'raw':
            return dat.find(tag)
        # NOTE: SWITCHED TXT TO STR AND DROPPED STR WITH MOVE TO PY35
        elif how is 'str':
            return dat.find(tag).text
        #elif how is 'str':
        #    return dat.find(tag).text.encode('ascii', 'ignore')
        elif how is 'all':
            return dat.findAll(tag)

    except AttributeError:
        return None

################################################################################################
################################## ERPSC - UTILS - DECORATORS ##################################
################################################################################################

def CatchNone(func):
    """Decorator function to catch and return None, if given as first argument."""

    def wrapper(*args):

        if args[0] is not None:
            return func(*args)
        else:
            return None

    return wrapper


def CatchNone2(func):
    """Decorator function to catch and return None, None if given as argument."""

    def wrapper(*args):

        if args[0] is not None:
            return func(*args)
        else:
            return None, None

    return wrapper
