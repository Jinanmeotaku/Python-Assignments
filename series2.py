#Given two integers A and B. Print all numbers from A to B inclusively, 
#in increasing order, if A < B, or in decreasing order, if A ≥ B.

def series2():
    A = int(input("Enter a number: "))
    B = int(input("Enter a number: "))

    if A < B:
        for i in range(A, B+1):
            print(i, end=" ")
    elif A >= B:
        for i in range(A, B-1, -1):       #B-1 because we want to include B in the range 
            print(i, end=" ")

series2()