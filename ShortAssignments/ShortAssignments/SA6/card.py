# Author: Rahul Gupta
# Date: 02/13/2023
# Purpose: Create a Card class.

class Card:

    def __init__(self, card, suit):
        self.suit_name = ["clubs", "spades", "diamonds", "hearts"]  # Create a list of suit names
        for i in range(1, 5):
            if suit == i:
                self.name_suit = self.suit_name[i-1]  # Assign suit names to entered numbers

        # Assign cards to the entered value of cards
        if 0 < card < 11:
            self.card = card
        elif card == 11:
            self.card = "Jack"
        elif card == 12:
            self.card = "Queen"
        elif card == 13:
            self.card = "King"

    def __str__(self):  # Return a string
        return str(self.card) + " of " + self.name_suit
