#Given a string in which the letter h occurs at least twice, 
# reverse the sequence of characters enclosed between the first and last occurrences of it.

#Criteria:

#Test #	Input	                                        Output
#1	In the hole in the ground there lived a hobbit      In th a devil ereht dnuorg eht ni eloh ehobbit

#2	qwertyhasdfghzxcvb                                  qwertyhgfdsahzxcvb

def reverseFragment():
    string = input("Enter a string:")
    first_occurance = string.find("h")
    last_occurance = string.rfind("h")
    print(string[:first_occurance + 1] + string[first_occurance:last_occurance][::-1] + string[last_occurance + 1:])