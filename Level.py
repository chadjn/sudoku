"""
Mardi 22 octobre 2019
Lucille Gueguen
"""

# classe correspondant au niveau de jeu de la grille de SUDOKU
class Level:

    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def setNumber(self, new_number):
        self.number = new_number