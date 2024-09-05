#Given a year (as a positive integer), find the respective number of the century. 
# Note that, for example, 20th century began with the year 1901.

def century():
    year = int(input("Enter a year: "))
    
    if year % 100 == 0:          #if the year is divisible by 100, it is the last year of the century
        print(year // 100)
    else:
        print(year // 100 +1)    #if the year is not divisible by 100, it is the first year of the next century

century()