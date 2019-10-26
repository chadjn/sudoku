"""Classe Column (colonne d'une grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Import de la classe abstraite
import GridPart
from GridPart import *

class Column(GridPart):

    # Fonction renvoyant le numéro de la colonne
    def getColumnNb(self):
        return self.getSquare(0).getCoordinates().getY()

    def afficherNb(self):
        print("Colonne n°{}".format(self.getColumnNb() + 1))
