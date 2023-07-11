# Author: Rahul Gupta
# Date: 02/13/2023
# Purpose: Create a Deck class.

from ShortAssignments.SA6.card import Card
from random import randint


class Deck:
    def __init__(self):
        self.card_list = []  # Create an empty card list

    def add_standard_cards(self):
        for suit in range(1, 5):
            for card in range(1, 14):
                self.card_list.append(Card(card, suit))  # Add all 52 standard cards to the list

    def shuffle(self):  # Method to reorder the cards randomly
        for i in range(0, 52):
            j = randint(0, 51)
            temp = self.card_list[i]
            self.card_list[i] = self.card_list[j]
            self.card_list[j] = temp

    def deal(self, count):  # Method to return and remove the last count cards from the deck
        hand = Deck()
        for i in range(count):
            if len(self.card_list) == 0:
                break
            hand.card_list.append(self.card_list.pop(-1))
        return hand
