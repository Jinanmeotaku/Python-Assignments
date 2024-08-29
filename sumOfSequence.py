
#Given a sequence of non-negative integers, where each number is written (input) 
# in a separate line. The sequence ends with 0. Print the sum of the sequence

def sumOfSequence():
    sum = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        sum += num
    print(sum)

sumOfSequence()