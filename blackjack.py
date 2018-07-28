''' This program creates a game of 21 Black Jack. Includes
    some guidance from the Think Python book. '''

import random


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __add__(self, other):
        sum = self.rank + other.rank
        return sum

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        cards = []
        for card in self.cards:
            cards.append(str(card))

        return '\n'.join(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove(self):
        self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

class Hand(Deck):

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        txt = 'Your hand:\n'
        for card in range(len(self.cards)):
            txt += str(self.cards[card]) + '\n'
        return txt

    def draw_card(self, deck):
        random.shuffle(deck.cards)
        self.cards.append(deck.cards.pop())

def game():
    print('This is 21 BlackJack!'.center(60, '*'))

    inpt = ''

    game_deck = Deck()
    hand = Hand(input('Enter Player Name: '))
    hand_2 = Hand('Dealer')

    #Game Logic
    while inpt != 'quit':
        move = input("Press 'Enter' to draw a card\n")
        hand.draw_card(game_deck)
        print(hand)
        move = input("Type 'draw' to draw a card or press 'Enter' to hold\n")

        #Move process - pops card from deck into hand and checks value
        if move == 'draw':
            hand.draw_card(game_deck)
            print(hand)
            if checker(hand) == 21:
                print('21 BlackJack! You win!')
                inpt = input("Enter Yes if you'd like to play again.\nEnter 'quit' to exit.\n")
                game_deck = Deck()
                hand.cards = []
                continue
            if checker(hand) > 21:
                print('You lose. You went over 21.')
                inpt = input("Enter 'Yes' if you'd like to play again.\nEnter 'quit' to exit.\n")
                game_deck = Deck()
                hand.cards = []
                continue
        else:
            pass

        #Move process
        move = input("Type 'draw' to draw a card or press 'Enter' to hold\n")
        if move == 'draw':
            hand.draw_card(game_deck)
            print(hand)
            if checker(hand) + hand.cards[2].value > 21:
                print('You lose. You went over 21.')
                inpt = input("Enter Yes if you'd like to play again.\nEnter 'quit' to exit.\n")
                game_deck = Deck()
                hand.cards = []
                continue
        else:
            pass

        #House draws cards based on how many you drew
        for card in range(len(hand.cards)):
            hand_2.draw_card(game_deck)
        house_cards = [str(i) for i in hand_2.cards]
        print('House Total:\n', checker(hand_2), '\n' + '\n'.join(house_cards))
        print()

        #Game results
        if checker(hand_2) > 21:
            print('You win!')
            break
        if checker(hand) > checker(hand_2):
            print('You win!')
        else:
            print('You lose!')

        #Restart game or exit
        inpt = input("Press 'Enter' if you'd like to play again.\nEnter 'quit' to exit.\n")
        game_deck = Deck()
        hand.cards = []
        hand_2 = []
        continue

def checker(item):
    # Checks total value of hand
    if len(item.cards) == 1:
        return item.cards[0].value
    try:
        return item.cards[0] + item.cards[1] + item.cards[2]
    except:
        return item.cards[0] + item.cards[1]

game()
