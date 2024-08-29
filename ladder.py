#for a iven integer n, write a function ladder(n) that prints a ladder of n steps.
# the k-th step consists of the integers from 1 to k without spaces between them.
#to do that you can use the sep and end arguments for the print function.

def ladder():
    n = int(input("Enter the number of steps: "))
    sum = 0
    for i in range (1, n+1):
        sum = sum * 10 + i           
        print(sum, sep = "", end = "\n")      #sep = "" removes the space between the numbers and end = "\n" prints the numbers in a new line

ladder()


#another way to solve the probelm is to use nested loops

def ladder():
    n = int(input("Enter the number of steps: "))
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = "")
        print()

ladder()

# the iteration broken down:
# for i = 1, j = 1, print 1
# for i = 2, j = 1, print 1
# for i = 2, j = 2, print 12
# for i = 3, j = 1, print 1
# for i = 3, j = 2, print 12
# for i = 3, j = 3, print 123
# for i = 4, j = 1, print 1
# for i = 4, j = 2, print 12
# for i = 4, j = 3, print 123
# for i = 4, j = 4, print 1234