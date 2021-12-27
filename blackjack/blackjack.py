import random
playerIn = True
dealerIn = True

deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
playerHand = []
dealerHand = []

#deal the card 
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calc total of hand
def total(turn):
    total = 0
    face = ['J','Q','K']
    for card in turn:
        if card in range (1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


#check winner
def revealDealerHand():
    if len(dealerHand) == 2 :
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0],dealerHand[1]


#game loop
for _ in range(2):
    dealCard(playerHand)
    dealCard(dealerHand)
    
    

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X,")
    print(f"You have {playerHand} Current Hand: {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) >= 17:
        dealerIn = False
    else:
        dealCard(dealerHand)
        print(f"Dealer now has {revealDealerHand()} ")
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
        print(f"player hits, current hand {total(playerHand)}")
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"\nYou have {playerHand} for a total of 21, dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("BJ YOU WIN")
elif total(dealerHand) == 21:
    print("Dealer wins with 21")
elif total(playerHand) > 21:
    print("you bust, dealer wins")
elif total(dealerHand) > 21:
    print("WIN, dealer busts, you win")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"LOSE, Dealer hand is better, {total(dealerHand)}")
elif 21 - total(dealerHand) > 21-total(playerHand):
    print(f"WIN,player hand is better, you win, {total(playerHand)}")





