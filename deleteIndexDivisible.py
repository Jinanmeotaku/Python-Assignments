#Given a string, delete all its characters whose indices are divisible by 3.

#Example input
#Python

#Example output
#yton

def deleteIndexDivisible():
    string = input("Enter a string:")
    new_string = ""
    for i in range (len(string)):
        if i % 3 != 0:
            new_string += string[i]
    print(new_string) 

deleteIndexDivisible()
