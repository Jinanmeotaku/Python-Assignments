#Write a program that takes in the user's name, which is taken in as input in all lower-case characters. 
# If the least significant bit of the ten's place digit of the ASCII representation of 
# the last character of the name matches with the least significant bit of the one's place digit of 
# the ASCII representation of the last character, print "Lsb matches: <tens lsb> <ones lsb>, 
# otherwise print "Lsb does not match: <tens lsb> <ones lsb>".

def lsbMatch():
    name = input("Enter your name: ")
    last_char = name[-1]
    tens_lsb = ord(last_char) // 10 % 2   #tens place digit of the binary representation of the ASCII value
    ones_lsb = ord(last_char) % 10 % 2    #one's place digit of the binary representation of the ASCII value
    if tens_lsb == ones_lsb:
        print(f"Lsb matches: {tens_lsb} {ones_lsb}")
    else:
        print(f"Lsb does not match: {tens_lsb} {ones_lsb}")

lsbMatch()
    