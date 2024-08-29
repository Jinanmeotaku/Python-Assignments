#There was a set of cards with numbers from 1 to N. One of the cards is now lost. 
# Determine the number on that lost card given the numbers for the remaining cards.
#Given a number N, followed by N − 1 integers representing the numbers on the 
# remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card

def lostCard():
    n = int(input("Enter a number:"))
    total_sum = n * (n + 1) // 2    #sum of all numbers from 1 to n
    current_sum = 0

    for i in range(n-1):
        current_sum += int(input())
    
    missing_card = total_sum - current_sum
    print(missing_card)

lostCard()