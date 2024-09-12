#Given a string in which the letter h occurs at least twice, 
# replace every occurrence of the letter h by the letter H, except for the first and the last ones.

def replaceInFragment():
    string = input("Enter a String: ")
    first_occurance = string.find("h")
    last_occurance = string.rfind("h")

    if first_occurance != -1 and last_occurance != -1 and first_occurance != last_occurance:
        print(string[:first_occurance + 1] + string[first_occurance + 1:last_occurance].replace("h", "H") + string[last_occurance:])
    else:

        print(string)

replaceInFragment()