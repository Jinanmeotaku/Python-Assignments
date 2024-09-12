#Given a string that may contain a letter f. Print the index of the first and last occurrence of f.
#If the letter f occurs only once, then output its index once. If the letter f does not occur, print -1.

#Criteria:

#Test #	Input	Output
#1	    comfort	    3
#2	    office	    1 2

def firstAndLastOccurance():
    word = input("Enter a word: ")
    first_letter = word.find("f")
    last_letter = word.rfind("f")

    if last_letter == first_letter:
        print(first_letter)

    else:
        print(first_letter, last_letter)

firstAndLastOccurance()

#another exercise
#Given a string that may contain a letter p. Print the index of the second occurrence of p. 
#If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2

def secondOccurance():
    word = input("Enter a word:")
    first_letter = word.find("p")
    second_letter = word.find("p", first_letter + 1)   

    if first_letter == -1:
        print(-2)
    elif second_letter == -1:
        print(-1)
    else:
        print(second_letter)

secondOccurance()