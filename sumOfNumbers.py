

#The first line of input contains the integer N, which is the number of integers to follow. 
# Each of the next N lines contains one integer. Print the sum of these N integers.

def sumOfNumbers():
    sum = 0
    n = int(input("Enter the number of integers: "))
    for i in range(n):
        num = int(input("Enter a number: "))
        sum += num
    print(sum)

sumOfNumbers()