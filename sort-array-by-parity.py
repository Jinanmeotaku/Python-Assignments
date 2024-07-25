
#function to compare the elements of the array and sort them by parity 

def sortArrayByParity(A):
    B = []
    for i in A:
        if i % 2 == 0:
            B.append(i)
    for i in A:
        if i % 2 != 0:
            B.append(i)
    return B

#taking input from the user
input_string = input("Enter an array of numbers with spaces: ")

#splitting the input string and converting it into a list of integers
A = [int(x) for x in input_string.split()]

#calling the function
print(sortArrayByParity(A))