#Given a string of four numbers, if the numbers are in ascending order, print "Sorted & even" 
# if the summation of all of the numbers is even, and "Sorted & odd" if the summation is odd. 
# If the numbers are not sorted, and the summation of all of the numbers is even, print "Unsorted & even', 
# and "Unsorted & odd" if the summation of all of the numbers is odd.

#Criteria:
#Test #	Input	Output
#1	    2 3 4 6	Sorted & odd
#2	    1 2 3 4	Sorted & even
#3	    8 7 18 20	Unsorted & odd
#4	    9 31 18 2	Unsorted & even

#IMPLEMENTATION

#function to check if the sum is even or odd
def evenOrOdd(sum):     
    if sum % 2 == 0:
        return "Even"
    else:
        return "Odd"

#main function that takes in the input and checks if the numbers are sorted or not 
#and calls the evenOrOdd function to check if the sum is even or odd
   
def evOdSoUns():
    numbers = input("Enter four numbers: ")
    numbers = numbers.split()

    sum = 0
    for i in numbers:
        sum +=int(i)

    sorted = True
    for i in range (len(numbers) -1):
        if numbers[i] > numbers[i + 1]:
            sorted = False
            break
    
    if sorted:
        print("Sorted & ", evenOrOdd(sum))
    else:
        print("Unsorted & ", evenOrOdd(sum))


evOdSoUns()