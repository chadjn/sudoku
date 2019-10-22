"""Classe Piece ("super-carré" de 9 cases sous-composant une grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Import de la classe abstraite
import GridPart
from GridPart import *

class Piece(GridPart):

    # Fonction renvoyant les coordonnées du centre du "super-carré"
    def getCenter(self):
        return self.getSquare(4).getCoordinates()