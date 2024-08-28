#This program answers the question: Given the integer N - the number of seconds that is passed since midnight 
# - how many full hours and full minutes are passed since midnight?

def hoursAndSeconds():
    n = int(input())
    hours = n // 3600
    min = n//60

    print(hours, min)

hoursAndSeconds()
    