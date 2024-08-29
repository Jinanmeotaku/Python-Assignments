#Given a sequence of non-negative integers, where each number is written (input) 
#in a separate line. The sequence ends with 0. Print the average of the sequence. 

def averageOfSequence():
    sum = 0
    count = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        count += 1
        sum += num
    print(sum/count)

averageOfSequence()