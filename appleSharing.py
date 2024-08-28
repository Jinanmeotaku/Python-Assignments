#this program solves the apple sharing problem 
#N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains 
#in the basket. How many apples will each single student get? How many apples will remain in the basket?

def appleSharing():
    n = int(input())
    k = int(input())

    print(k // n)
    print(k % n)

appleSharing()