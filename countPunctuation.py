# Description: This program counts the number of punctuation marks in a sentence entered by user.

def countPunctuation():
    n = input("Enter a sentence: ")
    count = 0

    for char in n:
        if not (char.isalnum() or char.isspace()):
            count += 1
    print(count)

countPunctuation()