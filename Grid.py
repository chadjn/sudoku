"""Classe Grid (grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Square
from Square import *

import Piece
from Piece import *

import Column
from Column import *

import Line
from Line import *

import Level
from Level import *

class Grid():
    def __init__(self, id, squares = []):
        self.id = id
        self.squares = squares
        self.pieces = []
        self.columns = []
        self.lines = []

    def getId(self):
        return self.id

    def setId(self, new_id):
        self.id = new_id

    # Fonction qui renvoie le tableau des cases
    def getSquares(self):
        return self.squares

    # Fonction qui renvoie une case particulière en fonction de sa place dans le tableau
    def getSquare(self, n):
        return self.squares[n]

    # Fonction qui ajoute une case (new_square) à la suite dans le tableau des cases
    def addSquare(self, new_square):
        self.squares.append(new_square)

    # Fonction qui renvoie le tableau des "super-carrés"
    def getPieces(self):
        return self.pieces

    # Fonction qui renvoie un "super-carré" particulier en fonction de sa place dans le tableau
    def getPiece(self, n):
        return self.pieces[n]

    # Fonction qui ajoute un "super-carré" (new_piece) à la suite dans le tableau des "super-carrés"
    def addPiece(self, new_piece):
        self.pieces.append(new_piece)

    # Fonction qui renvoie le tableau des colonnes
    def getColumns(self):
        return self.columns

    # Fonction qui renvoie une colonne particulière en fonction de sa place dans le tableau
    def getColumn(self, n):
        return self.columns[n]

    # Fonction qui ajoute une colonne (new_square) à la suite dans le tableau des colonnes
    def addColumn(self, new_column):
        self.columns.append(new_column)

    # Fonction qui renvoie le tableau des lignes
    def getLines(self):
        return self.lines

    # Fonction qui renvoie une ligne particulière en fonction de sa place dans le tableau
    def getLine(self, n):
        return self.lines[n]

    # Fonction qui ajoute une ligne (new_line) à la suite dans le tableau des lignes
    def addLine(self, new_line):
        self.lines.append(new_line)

    # Fonction qui vérifie que la partie n'est composée que de valeurs correctes ou manquantes
    def checked(self):
        checked = True
        i = 0

        while checked is True and i != len(self.squares):
            if not self.squares[i].isChecked() or self.squares[i].getValue() == 0:
                checked = False
            i += 1

    # Fonction qui vérifie que la partie n'est composée que de valeurs correctes
    def complete_checked(self):
        checked = True
        i = 0

        while checked is True and i != len(self.squares):
            if not self.squares[i].isChecked():
                checked = False
            i += 1