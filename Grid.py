"""Classe Grid (grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Square
from Square import *

import math
from math import sqrt


class Grid():
    def __init__(self, id, size, width, height, squares_to_add=[]):
        self.id = id
        self.size = size
        self.width = width
        self.height = height

        # Création d'un tableau de cases (ligne par ligne)
        self.squares = [[Square(width, height, Coordinates(i, j),
                                squares_to_add[Coordinates(i + 1, j + 1).fromCoordinatesToNumber(size)], [],
                                squares_to_add[Coordinates(i + 1, j + 1).fromCoordinatesToNumber(size)] != 0,
                                squares_to_add[Coordinates(i + 1, j + 1).fromCoordinatesToNumber(size)] != 0) for j in
                         range(size)] for i in range(size)]

        # Création d'un tableau de coordonnées des "super-carrés"
        self.pieces = [[Coordinates(k - (k % int(sqrt(size))) + i,
                                    int(sqrt(size)) * (k % int(sqrt(size))) + j) for j
                        in range(int(sqrt(size))) for i in range(int(sqrt(size)))] for k in range(size)]

        self.selected = None
        self.sketching = False

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

    # Fonction qui renvoie le tableau des "super-carrés"
    def getPieces(self):
        return self.pieces

    # Fonction qui renvoie un "super-carré" particulier en fonction d'une de ses cases
    def getPiece(self, square):
        for i in range(self.size):
            for j in range(self.size):
                if self.pieces[i][j].getX() == square.getCoordinates().getX() and self.pieces[i][j].getY() == square.getCoordinates().getY():
                    return self.pieces[i]

    def getSelected(self):
        return self.selected

    def setSelected(self, new_selected):
        self.selected = new_selected

    def isSketching(self):
        return self.sketching

    def setSketching(self, new_sketching):
        self.sketching = new_sketching

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
        end = False

        # La boucle continue à chercher tant qu'il n'a pas rencontré de valeur infirmante et qu'il reste des cases à vérifier
        while checked is True and end is False:
            for i in range(self.size):
                for j in range(self.size):
                    if not self.squares[i][j].isChecked():
                        checked = False
            end = True

        return checked

    # Fonction qui dessine la grille
    def drawGrid(self, win, clue, line_color, selected_color, default_color, trial_color, checked_color, unchecked_color):
        gap = self.width / self.size # Taille d'une case

        # Définition de la taille des lignes de séparation en fonction de ce qu'elles séparent (cases ou "super-carrés")
        for i in range(self.size + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, line_color, (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, line_color, (i * gap, 0), (i * gap, self.height), thick)

        # Dessin des cases selon qu'elles sont fixes ou non, vérifiées ou non, affichées avec aide ou non
        for i in range(self.size):
            for j in range(self.size):
                if clue and not self.squares[i][j].isFixed():
                    if self.squares[i][j].isChecked():
                        self.squares[i][j].drawSquare(win, trial_color, checked_color, selected_color, self.size)
                    else:
                        self.squares[i][j].drawSquare(win, trial_color, unchecked_color, selected_color, self.size)
                else:
                    self.squares[i][j].drawSquare(win, trial_color, default_color, selected_color, self.size)
