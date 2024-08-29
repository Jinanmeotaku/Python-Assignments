
#For a given integer X, find the greatest integer n where 2ⁿ is less than or equal 
# to X. Print the exponent value and the result of the expression 2ⁿ.

def powerOfTwo():
    num = int(input("Enter a number: "))

    n = 0
    while 2 ** n <= num:
        n += 1
    print(n-1, 2 ** (n-1))  #n-1 because the loop increments n by 1 before the condition is checked