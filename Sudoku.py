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
    def __init__(self, grid, player, timer, level, state = "new_game"):
        self.grid = grid
        self.player = player
        self.timer = timer
        self.level = level
        self.state = state

    def getGrid(self):
        return self.grid

    def setGrid(self, new_grid):
        self.grid = new_grid

    def getPlayer(self):
        return self.player

    def setPlayer(self, new_player):
        self.player = new_player

    def getTimer(self):
        return self.timer

    def setTimer(self, new_timer):
        self.timer = new_timer

    def getLevel(self):
        return self.level

    def setLevel(self, new_level):
        self.level = new_level

    def getState(self):
        return self.state

    def setState(self, new_state):
        self.state = new_state

    # Fonction qui permet de démarrer (ou reprendre) le jeu
    def start(self):

    # Fonction qui permet de mettre en pause le jeu
    def pause(self):

    # Fonction qui permet de supprimer le jeu en cours (vider les valeurs et les propositions, remettre le timer à zéro) et de le recommencer
    def reset(self):
        for i in range(0,9):
            for j in range(0,9):
                tmpSquare = Square(Coordinates(i,j))
                self.clearSquare(tmpSquare)
                self.clearTrials(tmpSquare)

    # Fonction qui permet d'ajouter une valeur à une case donnée
    def addValue(self, square, value):
        # Retrouver la case dans la grille
        # Ajouter la valeur à la case

    # Fonction qui permet d'ajouter une ou plusieurs proposition(s) à une case donnée
    def addTrial(self, square, trial):
        # Retrouver la case dans la grille
        # Ajouter les propositions à la case

    # Fonction qui permet d'effacer une case donnée (sa valeur et ses propositions)
    def clearSquare(self, square):
        # Retrouver la case dans la grille
        # Vider la case de sa valeur
        # Vider la case de ses propositions

    # Fonction qui permet d'effacer une proposition donnée dans une case donnée
    def removeTrial(self, square, trial):
        # Retrouver la case dans la grille
        # Supprimer la proposition donnée de la case

    # Fonction qui permet d'effacer toutes les propositions dans une case donnée
    def clearTrials(self, square):
        # Retrouver la case dans la grille
        # Vider la case de ses propositions