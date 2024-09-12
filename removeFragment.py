#Given a string in which the letter h occurs at least twice. 
# Remove from that string the first and the last occurrence of the letter h, 
#as well as all the characters between them.

#Criteria:

#Test   #	Input	                                    Output
#1	In the hole in the ground there lived a hobbit      In tobbit

#2	qwertyhasdfghzxcvb                                  qwertyzxcvb

def removeFragment():
    string = input("Enter a string:")
    first_occurance = string.find("h")
    last_occurance = string.rfind("h")
    print(string[:first_occurance] + string[last_occurance + 1:])

removeFragment()

