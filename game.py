from classes.deck import Deck
import os

def rules():
    os.system('cls')
    print('''
The goal is to be the first player to win all 52 cards

THE DEAL
The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.

THE PLAY
Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.

If the cards are the same rank, it is War. Each player turns up one card face down and one card face up. The player with the higher cards takes both piles (six cards). If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. The player with the higher card takes all 10 cards, and so on.

HOW TO KEEP SCORE
The game ends when one player has won all the cards.

Press any key to continue...
    ''')
    input()

def new_game():
    player = Deck()
    computer = Deck()
    player.randomize()
    computer.cards = player.split_deck()
    print_screen(computer, player)
    print("\nHit enter to draw\n")
    input()
    while len(player.cards) and len(computer.cards):
        print_screen(computer, player)
        print(f"Player: {player.cards[0].string_val} of {player.cards[0].suit}                   Computer: {computer.cards[0].string_val} of {computer.cards[0].suit}")
        print("\n\n")
        if player.cards[0].point_val > computer.cards[0].point_val:
            player.cards.append(computer.cards[0])
            computer.cards.pop(0)
            player.cards.append(player.cards[0])
            player.cards.pop(0)
            print("Player Won!")
        elif player.cards[0].point_val < computer.cards[0].point_val:
            computer.cards.append(player.cards[0])
            player.cards.pop(0)
            computer.cards.append(computer.cards[0])
            computer.cards.pop(0)
            print("Computer Won!")
        else:
            computer.cards.pop(0)
            player.cards.pop(0)
            print("TIE!")
        print("press enter to draw again...")
        input()
    if len(computer.cards):
        computer_won()
    else:
        player_won()

def print_screen(computer, player):
    os.system('cls')
    print(f'''
    Player 1                                   Computer
    Cards: {len(player.cards)}                                   {len(computer.cards)}
    ''')

def computer_won():
    os.system('cls')
    print("Computer Won the game!")
    print("Press enter to continue...")
    input()

def player_won():
    os.system('cls')
    print("You won the Game!")
    print("Press enter to continue...")
    input()

#---------------main
choice = ""
while (choice != "3"):
    os.system('cls')
    print("***WAR!***")
    print('''
    1 - What are the Rules?
    2 - Play
    3 - Quit
    ''')

    choice = input("Enter choice: ")
    if(choice=="1"):
        rules()
    elif(choice=="2"):
        new_game()
    elif(choice=="3"):
        break