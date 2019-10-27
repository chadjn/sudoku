import Column
from Column import *

import Coordinates
from Coordinates import *

import Grid
from Grid import *

import Level
from Level import *

import Line
from Line import *

import Piece
from Piece import *

import Player
from Player import *

import Square
from Square import *

import Sudoku
from Sudoku import *

import Timer
from Timer import *

coords = []
squares = []
for i in range(0,9):
    for j in range(0,9):
        coords.append(Coordinates(i, j))

# for c in coords:
#     c.afficher()

for i in range(0,len(coords)):
    squares.append(Square(coords[i], 0, []))

# for s in squares:
#     s.afficher()

column_squares = []
line_squares = []
i = 0
for s in squares:
    coord = s.getCoordinates()
    if coord.getX() == i:
        line_squares.append(s)

    if coord.getY() == i:
        column_squares.append(s)

column = Column(column_squares)
line = Line(line_squares)

piece_squares = []
i = 3
for s in squares:
    coord = s.getCoordinates()
    if (coord.getX() < i) and (coord.getY() < i):
        piece_squares.append(s)

piece = Piece(piece_squares)

grid = Grid(1, squares)
grid.addColumn(column)
grid.addLine(line)
grid.addPiece(piece)

level = Level(1)
player = Player("Charlotte")
timer = Timer()

sudoku = Sudoku(grid, timer)

