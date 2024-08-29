#this program finds the least divisor of a number entered by the user
def leastDivision():
    num = int(input("Enter a number: "))
    divisor = 2

    while num % divisor != 0:
        divisor += 1
    print(divisor)

leastDivision()