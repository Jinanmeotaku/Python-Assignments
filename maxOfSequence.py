#Given a sequence of non-negative integers, where each number is written (input) 
# in a separate line. The sequence ends with 0. Print the maximum of the sequence.

def maxOfSequence():
    max = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        if num > max:     #if the number entered is greater than the current max
            max = num      #then the number entered becomes the new max
    print(max)

maxOfSequence()