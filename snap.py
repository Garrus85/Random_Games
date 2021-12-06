# Game 2: SNAP card game
""" Created the basic SNAP game utilising objects"""

import random
import time


class Card:

    def __init__(self, suit, value):
        self.suit = suit.capitalize()
        self.value = value

    def __str__(self):
        return (f'{self.value} {self.suit}')

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value


class Deck:

    def __init__(self):
        self.deck = []

    def generate_deck(self):
        for i in ["He", "Cl", "Di", "Sp"]:
            for j in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
                card = Card(i, j)
                self.deck.append(card)

    def show_deck(self):
        deck_string = ""
        for i in self.deck:
            deck_string = deck_string + "[" + i.__str__() + "]" + " "
        print(deck_string)

    def deck_size(self):
        return len(self.deck)

    def draw_card(self):
        x = len(self.deck)
        idx = random.randint(0, x-1)
        card = self.deck[idx]
        self.deck.remove(card)
        return card



def game(player1, player2):

    winner = False
    pile = []
    p2_card = player2.draw_card()
    pile.append(p2_card)
    print(p2_card)
    time.sleep(1)

    while winner == False:

        p1_card = player1.draw_card()
        print(f'P1: {p1_card}')
        prev_card = pile[-1]
        time.sleep(1)
        if p1_card.get_value() == prev_card.get_value():
            print("---- SNAP! ----")
            time.sleep(1)
            print(" Player 1 WINS!")
            winner = True
        else:
            pile.append(p1_card)

        p2_card = player2.draw_card()
        print(f'P2: {p2_card}')
        prev_card = pile[-1]
        time.sleep(1)
        if p2_card.get_value() == prev_card.get_value():
            print("---- SNAP! ----")
            print("Player 2 WINS!")
            winner = True
        else:
            pile.append(p2_card)

        cards_left = player2.deck_size()
        if cards_left == 0:
            print("Out of cards")
            break


def snap():

    #TODO: let player click or input when they see a duplicate
    #TODO change pause from drawing card to random amount
    p1 = Deck()
    p1.generate_deck()
    p2 = Deck()
    p2.generate_deck()

    game(p1, p2)


