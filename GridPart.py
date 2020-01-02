"""Classe GridPart (partie abstraite d'une grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports (abc importe la notion d'abstraction)
import abc

import Square
from Square import *

class GridPart(abc.ABC):

    # Initialisation de la partie abstraite par la création d'un tableau de cases
    def __init__(self, squares = []):
        self.squares = squares

    # Fonction qui renvoie le tableau des cases
    def getSquares(self):
        return self.squares

    # Fonction qui renvoie une case particulière en fonction de sa place dans le tableau
    def getSquare(self, n):
        return self.squares[n]

    # Fonction qui ajoute une case (new_square) à la suite dans le tableau des cases
    def addSquare(self, new_square):
        self.squares.append(new_square)

    # Fonction qui vérifie que la partie n'est composée que de valeurs correctes ou manquantes
    def checked(self):
        checked = True
        i = 0

        # La boucle continue à chercher tant qu'il n'a pas rencontré de valeur infirmante et qu'il reste des cases à vérifier
        while checked is True and i != len(self.squares):

            # Si la case n'est ni valide, ni nulle alors elle est erronée
            if not (self.squares[i].isChecked() or self.squares[i].getValue() == 0):
                checked = False
            i += 1

        return checked

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
