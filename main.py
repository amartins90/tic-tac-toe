# Tic Tac Toe
# Bot x Bot implementation

import random

class TicTacToe:
    def __init__(self):
        print('Initiating game...')
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.turn = self.defineStartingPlayer()
        while (self.gameContinue()):
            self.move()

    def defineStartingPlayer(self):
        return random.choice(['X', 'O'])

    def getMoveCoordinates(self):
        line = random.randint(0, 2)
        column = random.randint(0, 2)
        return line, column

    def move(self):
        line, column = self.getMoveCoordinates()
        if self.board[line][column] is None:
            print('Player ' + self.turn + ' turn')
            self.board[line][column] = self.turn;
            self.printBoard()
            self.changePlayer()
            return
        self.move()

    def changePlayer(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
             self.turn = 'X'

    def printBoard(self):
        for i in range(3):
            print('| ' + ' | '.join(field if field is not None else ' ' for field in self.board[i]) + ' | ')

    def gameContinue(self):
        # Horizontal
        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] is not None):
            print('Player ' + self.board[0][0] + ' wins!')
            return False
        if (self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] is not None):
            print('Player ' + self.board[1][0] + ' wins!')
            return False
        if (self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] is not None):
            print('Player ' + self.board[2][0] + ' wins!')
            return False

        # Vertical
        # 0,0 1,0 2,0
        # 0,1 1,1 2,1
        # 0,2 1,2 2,2
        if (self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] is not None):
            print('Player ' + self.board[0][0] + ' wins!')
            return False
        if (self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] is not None):
            print('Player ' + self.board[0][1] + ' wins!')
            return False
        if (self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] is not None):
            print('Player ' + self.board[0][2] + ' wins!')
            return False

        # Diagonal
        # 0,0 1,1 2,2
        # 0,2 1,1 2,0
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None):
            print('Player ' + self.board[0][0] + ' wins!')
            return False
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None):
            print('Player ' + self.board[0][2] + ' wins!')
            return False

        for line in self.board:
            for field in line:
                if field is None:
                    return True
        print('Draw!')
        return False

if __name__ == '__main__':
    t = TicTacToe()
