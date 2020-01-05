"""Classe Grid (grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Square
from Square import *

import math
from math import sqrt

class Grid():
    def __init__(self, id, size, width, height, squares_to_add = []):
        self.id = id
        self.size = size
        self.width = width
        self.height = height
        self.squares = [[Square(width, height, Coordinates(i,j), squares_to_add[Coordinates(i+1,j+1).fromCoordinatesToNumber(size)], [], squares_to_add[Coordinates(i+1,j+1).fromCoordinatesToNumber(size)] != 0, squares_to_add[Coordinates(i+1,j+1).fromCoordinatesToNumber(size) != 0]) for j in range(size)] for i in range (size)]
        self.selected = None

    def getId(self):
        return self.id

    def setId(self, new_id):
        self.id = new_id

    def getSize(self):
        return self.size

    def setSize(self, new_size):
        self.size = new_size

    def getWidth(self):
        return self.width

    def setWidth(self, new_width):
        self.width = new_width

    def getHeight(self):
        return self.height

    def setHeight(self, new_height):
        self.height = new_height

    # Fonction qui renvoie le tableau des cases
    def getSquares(self):
        return self.squares

    # Fonction qui renvoie une case particulière en fonction de sa place dans le tableau
    def getSquare(self, x, y):
        return self.squares[x][y]

    def getSelected (self):
        return self.selected

    def setSelected (self, new_selected):
        self.selected = new_selected

    # Fonction qui renvoie une liste de coordonnées de case selon qu'elles sont correctes ou non
    def listOfSquaresByChecked(self, checked):
        list = []
        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j].isChecked() == checked and not self.squares[i][j].isFixed() and self.squares[i][j].getValue() != 0:
                    list.append(self.squares[i][j].getCoordinates())
        return list

    # Fonction qui vérifie que la partie n'est composée que de valeurs correctes
    def complete_checked(self):
        checked = True

        # La boucle continue à chercher tant qu'il n'a pas rencontré de valeur infirmante et qu'il reste des cases à vérifier
        while checked is True:
            for i in range(self.size):
                for j in range(self.size):
                    if not self.squares[i][j].isChecked():
                        checked = False

        return checked

    def drawGrid(self, win):
        gap = self.width / 9
        for i in range(self.size + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.size):
            for j in range(self.size):
                self.squares[i][j].drawSquare(win)
