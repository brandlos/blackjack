import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        dealt = deck.pop()
        hand.append(dealt)
    return hand


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def hit(hand):
    dealt = deck.pop()
    hand.append(dealt)
    return hand


def score(dealer, player):
    player_score = total(player)
    dealer_score = total(dealer)
    print("\nDealer's hand includes: " + str(dealer[0]))
    print("Your hand includes: " + str(player) +
          ". Your score is now " + str(player_score) + ".")
    if player_score == 21 and player_score == dealer_score:
        print("\nGAME OVER: You both score 21; it's a tie.")
        reset()
    elif player_score == 21:
        print("\nGAME OVER: You've got a Blackjack; you win.")
        reset()
    elif dealer_score == 21:
        print("\nGAME OVER: Dealer's hand is :" + str(dealer) +
              ". They've got a Blackjack; dealer wins.")
        reset()
    elif player_score > 21:
        print("\nGAME OVER: You bust; dealer wins.")
        reset()
    elif dealer_score > 21:
        print("\nGAME OVER: Dealer's hand is: " +
              str(dealer) + ". Dealer busts; you win.")
        reset()
    elif dealer_score > 17:
        print("\nGAME OVER:\nDealer's hand: " + str(dealer) +
              ". Dealer's score: " + str(dealer_score) + ".")
        print("Player's hand: " + str(player) +
              ". Player's score: " + str(player_score) + ".")
        if player_score > dealer_score:
            print("You win.")
        elif dealer_score > player_score:
            print("Dealer wins.")
            reset()
        else:
            print("Tie game.")
        reset()


def reset():
    choice = input("\nPlay again? [Y/N] >> ").lower()
    if choice == "y":
        dealer = []
        player = []
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4
        blackjack()
    elif choice == "n":
        print("Quitting application.")
        exit()


def blackjack():
    choice = True
    print("Welcome to Blackjack; bienvenidos a veintiuno! Let's deal some cards:\n")
    dealer = deal(deck)
    player = deal(deck)
    score(dealer, player)
    while choice != "q":
        choice = input("Will you [H]it, [S]tand, or [Q]uit? >> ").lower()
        if choice == "h":
            hit(player)
            hit(dealer)
            score(dealer, player)
        elif choice == "s":
            hit(dealer)
            score(dealer, player)
        elif choice == "q":
            print("Quitting application.")
            exit()


blackjack()
