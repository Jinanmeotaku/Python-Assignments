#Given five integers, print the least of them.

#Example input
#10
#20
#30
#40
#50

#Example output
#10

def minOfFiveNums():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = int(input("Enter another number: "))
    d = int(input("Enter another number: "))
    e = int(input("Enter another number: "))

    if a < b and a < c and a < d and a < e:
        print(a)
    elif b < a and b < c and b < d and b < e:
        print(b)
    elif c < a and c < b and c < d and c < e:
        print(c)
    elif d < a and d < b and d < c and d < e:
        print(d)
    else:
        print(e)
    
minOfFiveNums()
