#Given a sequence of non-negative integers, where each number is written (input) in 
# a separate line. Determine the length of the sequence. 
# The sequence ends with 0. Print the length of the sequence (not counting the 0).
#  The numbers following the number 0 should be omitted.

def lengthOfSequence():
    length = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        length += 1
    print(length)

lengthOfSequence()

#Note: although the problem question makes it seem like there is more numbers 
# to be entered after 0, the program stops taking input after 0 is entered.
