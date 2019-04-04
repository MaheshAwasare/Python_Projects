# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:56:12 2019

@author: Mahesh
"""

def check(fileName):
    with open(fileName) as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if 'file2' in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding

print(check('sample.txt'))