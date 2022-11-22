import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

#this is allowing all players to get their next move given a game
    def get_move(self, game):
        pass #passing in the game


#using inheritance to create a random computer player and a human player
#by building ontop of the base player and using player as the superclass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player)
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass