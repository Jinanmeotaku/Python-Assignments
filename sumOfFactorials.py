#In mathematics, the factorial of an integer n, denoted by n! is the following product:
#n! = 1 × 2 × … × n
#For the given integer n calculate the value n!. Don't use the math module in this exercise.

def sumOfFactorials():
    n = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)

sumOfFactorials()

#In mathematics, the factorial of an integer n, denoted by n! is the following product:
#n! = 1 × 2 × … × n
#For the given integer n calculate the value
#1! + 2! + 3! + ... + n!
#Try to discover the solution that uses only one for-loop. And don't use the math module in this exercise.

def sumOfFactorials():
    n = int(input("Enter a number:"))
    factorial = 1
    sum = 0
    for i in range(1, n+1):
        factorial *= i 
        sum += factorial
    print(sum)

sumOfFactorials()