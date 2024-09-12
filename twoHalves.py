#Given a string, cut it into two equal parts. 
# If the length of the string is odd, leave the middle character within the first chunk, 
# so that the first string contains one more character than the second. 
# Now print a new string on a single row with the first and second halves swapped: second half first and the first half last.

#Can you solve it without using if?

#Criteria:

#Test #	Input	Output
#1	Qwerty      rtyQwe
#2	Hi	        iH

def twoHalves():
    string = input("Enter a string:")
    mid = (len(string) + 1) // 2        #this gets the middle character of the string as an integer
    first_half = string[:mid]           #this gets the first half of the string as a string
    second_half = string[mid:]          #this gets the second half of the string as a string

    print(second_half + first_half)

twoHalves()