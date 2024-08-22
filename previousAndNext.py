# Description: Given an integer, print its previous and next numbers.

def previousAndNext():
    num = int(input())
    next = num + 1
    previous = num - 1
    print("The next number for the number " + str(num) + " is " + str(next))   #str() is used to convert the integer to a string
    print ("The previous number for the number " + str(num) + " is " + str(previous))

previousAndNext()