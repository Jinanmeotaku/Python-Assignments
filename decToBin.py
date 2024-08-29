# this program converts a deciaml number to binary 

def decToBin():
    n = int(input("Enter a number: "))
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str #add the remainder to the left of the string
        n = n // 2
    return binary_str

print(decToBin())

#This code does the opposite of the previous code. 
# It converts a binary number to decimal

def binToDec():
    s = input("Enter a binary number: ")
    decimal = 0
    for i in range(len(s)):
        decimal += int(s[i]) * 2 ** (len(s) - i - 1)
    return decimal

print(binToDec())

