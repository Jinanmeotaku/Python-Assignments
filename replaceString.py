#Given a string. Replace in this string all the numbers 1 by the word one.

#Criteria:

#Test #	Input	Output
#1	    1+1=2   one+one=2

#2	Hello, 2345678990   Hello, 2345678990

def replaceString():
    string = input("Enter a string:")
    print(string.replace("1", "one"))
    