"""
Mardi 22 octobre 2019
Léa Dollé
"""

# classe définissant le joueur du sudoku
class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getScore(self):
        return self.score

    def setScore(self, new_score):
        self.score = new_score