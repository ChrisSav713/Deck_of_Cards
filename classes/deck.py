from . import card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                point_val = i
                if i == 1:
                    str_val = "Ace"
                    point_val = 13
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , point_val , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
    
    def empty_deck(self):
        self.cards.clear()

    def randomize(self):
        new_deck = Deck()
        new_deck.empty_deck()
        while len(self.cards):
            random_number = random.randrange(0,len(self.cards))
            new_deck.cards.append(self.cards[random_number])
            self.cards.pop(random_number)
        self.cards = new_deck.cards

    def split_deck(self):
        new_deck = Deck()
        new_deck.empty_deck()
        while len(self.cards) > 26:
            random_number = random.randrange(0,len(self.cards))
            new_deck.cards.append(self.cards[random_number])
            self.cards.pop(random_number)
        return new_deck.cards
