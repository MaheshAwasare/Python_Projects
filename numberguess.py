# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 07:05:07 2019

Guess the number project

@author: Mahesh
"""
import random

userNum = input("what would be next number, guess between 1 to 10?   ")

sysnum= random.randint(1,10)

if userNum==sysnum:
    print(" You guessed it right, Guesser!!")
else:
    print("Nope. But system number is ",sysnum)    