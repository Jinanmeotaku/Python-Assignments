#Given a string input, determine if the string is a valid hexadecimal string. 
# Print True if it is, print False otherwise.

#Info: Hexadecimal is an alternate counting scheme, similar to binary numbers. 
# However, while binary numbers are 2-based (0 & 1 are the only digits), 
# hexadecimal are 16-based. Since we only have 0 - 9, 
# we use the letters a - f to represent an additional 6 characters to get to 16. 
# Once we count to 15 => "f", we then move to the next hexadecimal place: 16 => "10". 
# Going backwards, "11a" => 1 * 162 + 1 * 161 + 10 *160 = 282.

#Test #	Input (input())	Output (print())
#1	    11a             True
#2	    abcdefg         False

import string

def validHexString():
    hex_num = input("Enter a string:")
    for i in hex_num:
        if i not in string.hexdigits:
            print(False)
            return  
    print(True)

validHexString()


