#Given an integer greater than 9, print the number created by reversing the bits. 
# Combine the reversed bits to create the decimal value represented by the reversed bits 
# and print the decimal value.

 #Example input
#3

#Example output
#3

#Example input
#37

#Example output
#41

def reverseTheBits():
    number = int(input("Enter a number greater than 9: "))

    #printing the binary number
    binary_str = ""
    while number > 0:
        remainder = number % 2
        binary_str = str(remainder) + binary_str 
        number = number // 2
    
    #reversing the bits
    reversed_str = binary_str[::-1]
    #print decimal number of reversed bits
    decimal = 0
    for i in range(len(reversed_str)):
        decimal += int(reversed_str[i]) * 2 ** (len(reversed_str) - i - 1)
    print(decimal)

reverseTheBits()