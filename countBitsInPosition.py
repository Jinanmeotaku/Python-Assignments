#Given five input numbers, a, b, c, d and n, 
# print out the number of 1 bits at the nth least significant bit position in all four numbers a, b, c, d.
#Example input I
#1 1 1 1 0

#Example output
#4

#All numbers a, b, c and d are 1 - binary equivalent of which is 0001. 
# Since n is 0 in the input, nth lsb position is the last bit position.
# In all four numbers, the last bit position is 1, counting them results in 4.

#function that solves using remiander operator
def countBitsInPosition():
    number = input("Enter five numbers: ")
    number = number.split()

    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    d = int(number[3])
    n = int(number[4])

    count = 0
    
    count += (a >> n) & 1     #the math is a // 2^n and then & 1 to get the remainder
    count += (b >> n) & 1
    count += (c >> n) & 1
    count += (d >> n) & 1

    print(count)
    

countBitsInPosition()
