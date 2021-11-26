#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def add(file, path : str = ""):
    """add a relative import from the current repository of file
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
        file (str): The relative file. Put : __file__ 
        path (str, optional): Specify it to explore from your file Work like cd command of linux, example : '..' to go back. Defaults to "".

    Returns:
        [type]: [description]
    """
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(file)), path))
