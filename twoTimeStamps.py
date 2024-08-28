#This program answers the quuestion:Given two timestamps of the same day: a number of hours, 
# minutes and seconds for both of the timestamps. the moment of the first timestamp happened before the moment 
# of the second one. calculate how many seconds passed between them.

def twoTimeStamps():
    hour1 = int(input()) * 3600
    min1 = int(input()) * 60
    sec1 = int(input())

    hour2 = int(input()) * 3600
    min2 = int(input()) * 60
    sec2 = int(input())

    result = (hour2 - hour1) + (min2 - min1) + (sec2 - sec1)
    print(result)

twoTimeStamps()