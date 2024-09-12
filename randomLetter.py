#Given a string, return a random character from the string. 
# Note: The random library is, well, random. 
# We use the random.seed() function to make the tests consistent across use. 
# However, there may be some issues when using random numbers. 
#Test #	Input	                    Output
#1	"Python Rocks!" (Seed: 1)	    t(The output is random, but seed 1 should be consistent across Python versions)

#2	"Random Str" (Seed: 2)          R

import random

def randomLetter():
    random.seed(1)       #seed is used to make the output consistent
    string = input("Enter a string:")
    print(random.choice(string))       #selects a random character from the string

randomLetter()
