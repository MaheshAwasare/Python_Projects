# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:57:36 2019

@author: Mahesh
"""

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
 
def getNamedEntities(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity=" ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk=[]
            else:
               continue
           
    return continuous_chunk   

def check(fileName):
    with open(fileName) as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if 'file2' in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding


        
txtmsg = "Credit Suisse announced today the creation of Asia Pacific Trading Solutions (ATS) to capitalize on the significant opportunity across the region and further build on the success of the International Trading Solutions (ITS) business."
print(getNamedEntities(txtmsg))
