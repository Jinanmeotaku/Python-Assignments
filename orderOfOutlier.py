#Given three integers, in which two are equal to each other and the third one is different. 
# Print the order number of this different one - 1, 2 or 3.

def orderOfOutlier():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    
    if a == b:
        print(3)
    elif a == c:
        print(2)
    else:
        print(1)