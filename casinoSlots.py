# Description: A simple casino slots game that takes user input for bets and outputs the results of each spin. 
# The game continues until the user types "DONE" and then the total winnings/losses are displayed.

import random
def casinoSlots():
    random.seed(0)
    total = 0
    while True:
        bet = input("Bet: ")
        if bet == "DONE":
            break
        bet = int(bet)
        slot1 = random.randint(1, 7)
        slot2 = random.randint(1, 7)
        slot3 = random.randint(1, 7)
        if slot1 == slot2 == slot3 == 7:
            winnings = bet * 7
        elif slot1 == slot2 == slot3:
            winnings = bet * 3
        elif slot1 == slot2 or slot2 == slot3:
            winnings = bet * 2
        else:
            winnings = -bet
        print(slot1, slot2, slot3, winnings)
        total += winnings
    print(total)
casinoSlots()