"""Classe Sudoku
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Grid
from Grid import *

class Sudoku():

    # Initialisation avec un état de jeu
    def __init__(self, grid):
        self.grid = grid

    def getGrid(self):
        return self.grid

    def setGrid(self, new_grid):
        self.grid = new_grid

    # Fonction qui permet d'ajouter une valeur à une case donnée
    def addValue(self, square, value):
        for s in self.grid.getSquares():
            if s.getCoordinates() == square.getCoordinates():
                s.setValue(value)

    # Fonction qui permet d'ajouter une proposition à une case donnée
    def addTrial(self, square, trial):
        for s in self.grid.getSquares():
            if s.getCoordinates() == square.getCoordinates():
                s.addTrial(trial)

    # Fonction qui permet d'effacer une case donnée (sa valeur et ses propositions)
    def clearSquare(self, square):
        self.clearTrials(square)
        for s in self.grid.getSquares():
            if s.getCoordinates() == square.getCoordinates():
                s.clearValue()

    # Fonction qui permet d'effacer une proposition donnée dans une case donnée
    def removeTrial(self, square, trial):
        for s in self.grid.getSquares():
            if s.getCoordinates() == square.getCoordinates():
                if s.haveTrial(trial):
                    s.clearTrial(trial)

    # Fonction qui permet d'effacer toutes les propositions dans une case donnée
    def clearTrials(self, square):
        for s in self.grid.getSquares():
            if s.getCoordinates() == square.getCoordinates():
                s.clearTrials()