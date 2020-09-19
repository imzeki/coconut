"""
Backend for Coconut
"""
import os
import pathlib

def getTypeOnly(find:type, l:list) -> list:
    """
    Gets the type wanted from a list
    """
    if type(find) != type:
        raise TypeError('Type given is not a type')
    elif type(l) != list:
        raise TypeError(f'{l} is not a list')
    else:
        return [f for f in l if type(f) == find]

def throwback():
    """
    Changes path back to parent path
    """
    os.chdir(pathlib.Path(__file__).parent)
    return pathlib.Path(__file__).parent

def trim(String:str):
    """
    Gets rid of all spaces in the string
    """
    return ''.join([s for s in str(String) if s != " "])