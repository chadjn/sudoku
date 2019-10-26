"""
Léa Dollé
Mardi 22 octobre 2019
classe coordonnées
"""

# Léa
# classe permettant de lire les coordonnées attribuées au cases
class Coordinates:

    def __init__(self, x, y):  # initialisation des coordonnées dans la classe
        self.x = x
        self.y = y

    def getX(self):  # fonction pour que la classe lise X
        return self.x

    def setX(self, new_x):  # fonction pour changer la valeur de x
        self.x = new_x

    def getY(self):
        return self.y

    def setY(self, new_y):
        self.y = new_y

    def afficher(self):
        print("({},{})".format(self.x, self.y))