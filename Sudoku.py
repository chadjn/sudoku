"""Classe Sudoku
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Grid
from Grid import *

import Player
from Player import *

import Timer
from Timer import *

import Level
from Level import *

class Sudoku():

    # Initialisation avec un état de jeu
    def __init__(self, grid, timer, state="new_game"):
        self.grid = grid
        self.timer = timer
        self.state = state

    def getGrid(self):
        return self.grid

    def setGrid(self, new_grid):
        self.grid = new_grid

    def getTimer(self):
        return self.timer

    def setTimer(self, new_timer):
        self.timer = new_timer

    def getState(self):
        return self.state

    def setState(self, new_state):
        self.state = new_state

    # Fonction qui permet de démarrer (ou reprendre) le jeu
    def start(self):
        if self.state != "new_game" and self.state != "paused":
            if self.state == "game_over":
                return self.reset()
        self.state = "running"
        self.timer.start()

    # Fonction qui permet de mettre en pause le jeu
    def pause(self):
        self.state = "paused"
        self.timer.pause()

    # Fonction qui permet de supprimer le jeu en cours (vider les valeurs et les propositions, remettre le timer à zéro) et de le recommencer
    def reset(self):
        self.state = "new_game"
        self.timer.reset()
        for i in range(0, 9):
            for j in range(0, 9):
                tmpSquare = Square(Coordinates(i, j))
                self.clearSquare(tmpSquare)
                self.clearTrials(tmpSquare)

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
                s.clearTrial(trial)

    # Fonction qui permet d'effacer toutes les propositions dans une case donnée
    def clearTrials(self, square):
        for s in self.grid.getSquares():
            if s.getCoordinates() == square.getCoordinates():
                s.clearTrials()

    def afficher(self):
        print("Le sudoku joue la grille n°{} depuis {}:{} (état = {}) :".format(self.getGrid().getId(), self.getTimer().getMinutes(), self.getTimer().getSecondes(), self.getState()))
        self.getGrid().afficher()