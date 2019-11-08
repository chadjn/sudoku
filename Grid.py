"""Classe Grid (grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Square
from Square import *

import math
from math import sqrt

class Grid():
    def __init__(self, id, squares = []):
        self.id = id
        self.squares = squares

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

    # Fonction qui renvoie une liste de coordonnées de case selon qu'elles sont correctes ou non
    def listOfSquaresByChecked(self, checked):
        list = []
        for s in self.squares:
            if s.isChecked() == checked and not s.isFixed() and s.getValue() != 0:
                list.append(s.getCoordinates())
        return list

    # Fonction qui vérifie que la partie n'est composée que de valeurs correctes
    def complete_checked(self):
        checked = True
        i = 0

        # La boucle continue à chercher tant qu'il n'a pas rencontré de valeur infirmante et qu'il reste des cases à vérifier
        while checked is True and i != len(self.squares):
            if not self.squares[i].isChecked():
                checked = False
            i += 1

        return checked

    def afficher(self):
        print("Grille n°{} :".format(self.getId()))
        for s in self.getSquares():
            s.afficher()

    def afficherSquare(self, n):
        self.getSquare(n).afficher()