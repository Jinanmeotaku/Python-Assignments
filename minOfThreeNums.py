#Given three integers, print the least of them. use compound boolean expressions.

def minOfThreeNums():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = int(input("Enter another number: "))
    
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c)

minOfThreeNums()
