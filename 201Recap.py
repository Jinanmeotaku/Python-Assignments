#Given a string of four numbers, print "Even" if the summation of all of the numbers is even, and "Odd" if the summation is odd.

#Criteria:
#Test #	Input	Output
#1	    2 3 4 6	    Odd
#2	    1 2 3 4	    Even
#3	   8 7 18 20	Odd
#4	   9 31 18 2	Even

def evenOrOdd():
    numbers = input("Enter four numbers: ")  
    numbers = numbers.split()

    sum = 0
    for i in numbers:
        sum += int(i)

    if sum % 2 == 0:
        print("Even")
    else:
        print("Odd")
   
evenOrOdd()