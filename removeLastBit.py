#Given two input numbers, print out the two numbers with their binary value shifted to the right by 1 bit.

#Criteria:
#Test #	Input	Output
#1	    3 5	        1 2
#2	    6 8	        3 4
#3	    5 8	        2 4
#4	    1 2         0 1
#5	    2 6         1 3
#6	    8 11        4 5
#7	    15 21       7 10
#8	    13 20       6 10

def shiftRight():
    number = input("Enter two numbers: ")
    number = number.split()

    num1 = int(number[0])
    num2 = int(number[1])

    num1 = num1 >> 1   #this interpreted into math is num1 // 2 
    num2 = num2 >> 1   #this interpreted into math is num2 // 2

    print(num1, num2)

shiftRight()




