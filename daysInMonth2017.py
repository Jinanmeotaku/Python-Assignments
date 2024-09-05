#Given a month - an integer from 1 to 12, print the number of days in it in the year 2017

def daysInMonth2017():
    month = int(input("Enter a month: "))
    
    if month == 2:
        print(28)
    elif month in [4, 6, 9, 11]:
        print(30)
    else:
        print(31)