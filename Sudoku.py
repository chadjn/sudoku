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
        for i in range(self.grid.getSize()):
            for j in range(self.grid.getSize()):
                if self.grid.getSquare(i,j).getCoordinates() == square.getCoordinates():
                    self.grid.getSquare(i,j).setValue(value)

    # Fonction qui permet d'ajouter une proposition à une case donnée
    def addTrial(self, square, trial):
        for i in range(self.grid.getSize()):
            for j in range(self.grid.getSize()):
                if self.grid.getSquare(i, j).getCoordinates() == square.getCoordinates():
                    self.grid.getSquare(i,j).addTrial(trial)

    # Fonction qui permet d'effacer une case donnée (sa valeur et ses propositions)
    def clearSquare(self, square):
        self.clearTrials(square)
        for i in range(self.grid.getSize()):
            for j in range(self.grid.getSize()):
                if self.grid.getSquare(i, j).getCoordinates() == square.getCoordinates():
                    self.grid.getSquare(i, j).clearValue()

    # Fonction qui permet d'effacer une proposition donnée dans une case donnée
    def removeTrial(self, square, trial):
        for i in range(self.grid.getSize()):
            for j in range(self.grid.getSize()):
                if self.grid.getSquare(i, j).getCoordinates() == square.getCoordinates():
                    if self.grid.getSquare(i, j).haveTrial(trial):
                        self.grid.getSquare(i,j).clearTrial(trial)

    # Fonction qui permet d'effacer toutes les propositions dans une case donnée
    def clearTrials(self, square):
        for i in range(self.grid.getSize()):
            for j in range(self.grid.getSize()):
                if self.grid.getSquare(i, j).getCoordinates() == square.getCoordinates():
                    self.grid.getSquare(i, j).clearTrials()

    def select(self, coord):
        for i in range(self.grid.getSize()):
            for j in range(self.grid.getSize()):
                self.grid.getSquare(i,j).setSelected(False)

        self.grid.getSquare(coord.getX(),coord.getY()).setSelected(True)
        self.grid.setSelected(coord)

    def click(self, pos):
        """
        :param: pos
        :return: coord
        """
        if pos[0] < self.grid.getWidth() and pos[1] < self.grid.getHeight():
            gap = self.grid.getWidth() / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return Coordinates(int(y), int(x))
        else:
            return None