'''
Dice Rolling simulator

'''
import random
roll ="Y"
while(roll=="Y"):
    roll = input("Do you want to roll the dice?   ")
    if roll=="Y":
        print("Your dice number is  ",random.randint(1,6))
