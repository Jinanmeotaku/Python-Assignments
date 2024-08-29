# Write a program to print the series of numbers from a to b. 
#this assumes th euser will enter two numbers a and b where a < b

def series():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    for i in range(a, b+1):
        print(i, end=" ")

series()


#to fix this to with a>b, we can use the following code 
def series():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    #if a is less than b, print the numbers from a to b
    if a < b:         
        for i in range(a, b+1):
            print(i, end=" ")
    
    #if a is greater than b, print the numbers from b to a
    else:
        for i in range(a, b-1, -1):
            print(i, end=" ")

series()