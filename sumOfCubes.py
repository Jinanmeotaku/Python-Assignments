#For the given integer N calculate the following sum:
#1³ + 2³ + ... + N³

def sumOfCubes():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    print(sum)

sumOfCubes()