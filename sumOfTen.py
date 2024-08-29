#10 numbers are given in the input. Read them and print their sum. 
#Use as few variables as you can.

def sumOfTen():
    sum = 0
    for i in range(10):
        num = int(input("Enter a number: "))
        sum += num
    print(sum)

sumOfTen()