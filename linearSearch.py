# this program is a simple linear search algorithm that searches for a number in a list of numbers
def linearSearch():
    search_num = int(input("Enter the number you want to search: "))
    numbers = []

    for i in range(8):
        num = int(input())
        numbers.append(num)
    
    if search_num in numbers:
        print(numbers.index(search_num))
    else:
        print("NOT FOUND")

linearSearch()


#a different approach
def linearSearch():
    search_term = int(input("Enter the number you want to search: "))
    found = False
    i = 0

    while found == False and i < 8:
        if int(input()) == search_term:
            print(i)
            found = True   
        i += 1
    if not found:
        print("NOT FOUND")

linearSearch()