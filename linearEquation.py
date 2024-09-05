#Write a program that solves a linear equation ax = b in integers. 
# Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" 
# or "many solutions" otherwise.

#Example input #1
#1

#-2

#Example output #1
#-2

def linearEquation():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    
    if a == 0 and b == 0:
        print("many solutions")
    elif a == 0:
        print("no solution")
    elif b == 0:
        print(0) 
    elif b % a != 0:
        print("no Solution")
    else:
        print(b // a)

linearEquation()