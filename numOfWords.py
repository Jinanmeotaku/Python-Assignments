#Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.

#Criteria:

#Test #	Input   	Output
#   Hello world       2
#2	Hello	          1
#3  q w e             3
#4	In the hole in the ground there lived a hobbit      10
#5	One two three four five                              5


def numOfWords():
    string = input("Enter a string: ")
    words = string.split()

    count = 0
    for i in words:
        count += 1
    print(count)

numOfWords()