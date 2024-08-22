#function to convert an excel column to a number
# for example, A -> 1, B -> 2, AA -> 27

def excel_column_to_number(column):
    total = 0
    power = 0
    for i in range(0, len(column)):
        power = len(column) - 1 - i                  #power of 26 for each character
        total += (ord(column[i]) - 64) * (26 ** power)  #converting the column to number
    
    return total

#taking input from the user
column = input("Enter the column name: ")

#calling the function
print(excel_column_to_number(column))
