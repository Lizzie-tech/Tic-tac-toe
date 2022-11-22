#define the class tic tac toe

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #making a list of length 9 to represent the board
        self.current_winner = None #this variable will track the winner and say who it is

    def print_board(self):
        for row in [self.board[i*3:(i+1)] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |') #seperators for each row

# ^ this function will print the board