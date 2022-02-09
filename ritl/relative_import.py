#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath, normpath
import sys, inspect

def add(file : str, path : str = "", verbose : bool = False):
    """@deprecated
    add a relative import from the current repository of file
    Is able to add a relative import from a sub repository thanks to path
    Examples :
         home
        |___data
        |   |___main.py
        |
        |___utils
            |___tools.py

        In > file = /home/data/main.py (executed from there)
             path = ""
        PathAppend(Out) > /home/data
        
        In > file = /home/data/main.py (executed from there)
             path = "../utils"
        PathAppend(Out) > /home/utils

    Args:
        file (str): The relative file. You have to put __file__ for the current file.
        path (str, optional): Specify it to explore from your file Work like cd command of linux, 
        example : '..' to go back. Defaults to "".

    """
    filedir = dirname(abspath(file))
    added_directory = normpath(join(filedir, path))
    if verbose:
        print(f"[ritl] - Current directory : {filedir}")
        print(f"[ritl] - Added directory : {added_directory}")
    sys.path.append(added_directory)
    
def add_rel_imp(path : str = "", verbose : bool = False):
    """add a relative import from the current file's directory
    Is able to add a relative import from a sub repository thanks to path
    Examples :
         home
        |___data
        |   |___main.py
        |
        |___utils
            |___tools.py

        In > file = /home/data/main.py (executed from there)
             path = ""
        PathAppend(Out) > /home/data
        
        In > file = /home/data/main.py (executed from there)
             path = "../utils"
        PathAppend(Out) > /home/utils

    Args:
        path (str, optional): Specify it to explore from your file Work like cd command of linux, 
        example : '..' to go back. Defaults to "".

    Returns:
        [type]: [description]
    """
    file = inspect.getmodule(inspect.stack()[-1][0]).__file__
    if verbose:
        print(f"[ritl] - Current file : {file}")
    add(file=file, path=path, verbose=verbose)