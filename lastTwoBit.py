#Given an integer greater than 9, print its last two bits with space in between.

#Example input
#   3

#Example output
# 1 1

#Example input
# 37

#Example output
# 0 1

 
#Criteria:
#Test #	Input	Output
#1      1234    1 0
#2      567     1 1


def lastTwoBit():
    number = input("Enter a number greater than 9: ")
    number = int(number)

    lastBit = number & 1
    secondLastBit = (number >> 1) & 1

    print(secondLastBit, lastBit)

lastTwoBit()

# now we want to print the decimal number of the last two bits in reverse order

#Example input
#   3
#Example output
#   3

def lastTwoBit():
    number = input("Enter a number greater than 9: ")
    number = int(number)

    lastBit = number & 1
    secondLastBit = (number >> 1) & 1

    newNumber = (lastBit << 1) + secondLastBit
    print(newNumber)

lastTwoBit()