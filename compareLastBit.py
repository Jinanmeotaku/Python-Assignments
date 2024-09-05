#Given two input numbers, print 'True' if the last least significant bit of the two number match and 'False' if they don't.

#Criteria:
#Test #	Input	Output
#1       3  5	True (because 3 is 0b11 and 5 if 0b101 - the lsb is 1 in both)

#2	     6  8	True (because 6 is 0b110 and 8 is 0b1000 - the lsb is 0 in both

#3	     5  8	False (because 5 is 0b101 and 8 is 0b1000 - the lsb is not the same

#4	     13 20  False

#5	     15 21  True

def compareLastBit():
    number = input("Enter two numbers: ")
    number = number.split()

    num1 = int(number[0])
    num2 = int(number[1])

    
    lsb1 = num1 % 2               #remainder of the number divided by 2 gives the least sig fig since its the last didgit in binary
    lsb2 = num2 % 2

    if lsb1 == lsb2:
        print("True")
        return
    else:
        print("False")
        return 

compareLastBit()
            

