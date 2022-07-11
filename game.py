from classes.deck import Deck
import os


print("********************************************")

player = Deck()
computer = Deck()

player.randomize()
computer = player.split_deck()

print("********Player*******************")
print(len(player.cards))
player.show_cards()
print("*******Computer******************************")
print(len(computer.cards))
computer.show_cards()