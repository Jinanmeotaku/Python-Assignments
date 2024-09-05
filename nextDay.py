#Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, 
# print the month and the day of the next day to it.

def nextDay():
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))
    
    if month == 2:                                     #if the month is February
        if day == 28:                                 
            print(month + 1, 1, sep = "\n")
        else:
            print(month, day + 1 , sep = "\n")        
    elif month in [4, 6, 9, 11]:                       #if the month has 30 days
        if day == 30:
            print(month + 1, 1, sep = "\n")
        else:
            print(month, day + 1, sep = "\n")
    elif month in [1, 3, 5, 7, 8, 10]:                #if the month has 31 days
        if day == 31:
            print(month + 1, 1, sep = "\n")
        else:
            print(month, day + 1, sep = "\n")
    else:                                             #if the month is December
        if day == 31 and month == 12:
            print(1, 1, sep = "\n")
        else:
            print(month, day + 1, sep = "\n")

nextDay()