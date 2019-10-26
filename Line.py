"""Classe Line (ligne d'une grille)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Import de la classe abstraite
import GridPart
from GridPart import *

class Line(GridPart):

    # Fonction renvoyant le numéro de la ligne
    def getLineNb(self):
        return self.getSquare(0).getCoordinates().getX()

    def afficherNb(self):
        print("Ligne n°".format(self.getLineNb() + 1))
