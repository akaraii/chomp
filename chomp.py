import numpy as np
import pandas as pd
import random

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self,size=(3,4)):
      self.p1=Player()
      self.p2=Player()
      self.turn=random.choice([self.p1,self.p2])

class Board:
    def __init__(self, rows, cols):
        # Use a 2d array to store board state
        # ones for chocolate, zeros for eaten squares, and -1 for poison
        self.rows = rows
        self.cols = cols
        self.state = np.ones((rows, cols), dtype=int)
        self.state[-1][0] = -1
    #to set up the game, arrange the number of rows(0-4) and coulumns(A-D)
    def __repr__(self):
        return f'Board({self.rows}, {self.cols})'

    def __str__(self):
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        for r in range(row+1):
            self.state[r][col:]=0

class Player:
    players = []
    name_1 = input("Enter a name")
    name_2 = input("Enter another a name")
    players.append(name_1)
    players.append(name_2)
    print("Player One is ", random.choice(players))
    def __init__(self, score=0,name=none):
        self.score=score
        self.name=input("Enter Your Name:")
    def __repr__(self):
        return f'player(score={self.score},name={self.name}'

