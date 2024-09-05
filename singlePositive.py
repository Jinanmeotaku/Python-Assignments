#Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.

def singlePositive():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    if a > 0 and b < 0:
        print("YES")
    elif a < 0 and b > 0:
        print("YES")
    else:
        print("NO")