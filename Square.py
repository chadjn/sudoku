"""
Mardi 22 octobre 2019
Lucille Gueguen et Léa Dollé
"""

# classe servant au carré de 9 cases/cellules
import pygame

import Coordinates
from Coordinates import *


class Square:

    def __init__(self, width, height, coordinates, value=0, trials=[], fixed=False, checked=False):
        self.width = width
        self.height = height
        self.selected = False

        self.value = value
        self.trials = trials
        self.fixed = fixed
        self.checked = checked
        self.coordinates = coordinates

    def getWidth(self):
        return self.width

    def setWidth(self, new_width):
        self.width = new_width

    def getHeight(self):
        return self.height

    def setHeight(self, new_height):
        self.height = new_height

    def isSelected(self):
        return self.selected

    def setSelected(self, new_selected):
        self.selected = new_selected

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value

    def getTrials(self):
        return self.trials

    def getTrial(self, n):
        return self.trials[n]  # accéder à un indice tu tableau

    def haveTrial(self, n):
        return any(t == n for t in self.trials)  # vérifier que la donnée existe

    def addTrial(self, new_trial):
        self.trials.append(new_trial)

    def isFixed(self):
        return self.fixed

    def setFixed(self, new_fixed):
        self.fixed = new_fixed

    def isChecked(self):
        return self.checked

    def setChecked(self, new_checked):
        self.checked = new_checked

    def getCoordinates(self):
        return self.coordinates

    def setCoordinates(self, new_coordinates):
        self.coordinates = new_coordinates

    def clearTrial(self, trial):
        self.trials.remove(trial)

    def clearTrials(self):
        self.trials.clear()

    def clearValue(self):
        self.value = 0

    def afficher(self, end):
        print(str(self.getValue()) + " ", end=end) # La variable end définit s'il faut sauter une ligne après la valeur

    def afficher_trials(self, line, end, fill):
        # Chaque emplacement a sa valeur propre, on vérifie donc que la valeur est présente pour l'afficher, sinon le brouillon est rempli par défaut (fill)
        print('[{}][{}][{}] '.format(3 * line - 2 if self.haveTrial(3 * line - 2) else fill,
                                     3 * line - 1 if self.haveTrial(3 * line - 1) else fill,
                                     3 * line if self.haveTrial(3 * line) else fill), end=end)

    # Fonction qui dessine la case dans PyGame
    def drawSquare(self, window, trial_color, value_color, selected_color, size):
        if self.fixed:
            fnt = pygame.font.Font('Carybe.otf', 20) # Si la case est fixe, elle a une police différente
        elif self.getValue() == 0:
            fnt = pygame.font.SysFont("Arial", 14) # Si l'entrée est un brouillon, la taille de police est plus petite
        else:
            fnt = pygame.font.SysFont("Arial", 20) # Police par défaut

        gap = self.width / size # gap définit la taille d'une case (taille de la grille divisée par le nombre de cases)
        x = self.getCoordinates().getY() * gap
        y = self.getCoordinates().getX() * gap

        # Définition du type d'entrée dans la case
        if self.getTrials() != [] and self.getValue() == 0: # Brouillon
            for t in self.trials:
                text = fnt.render(str(t), 1, trial_color) # Couleur des brouillons par défaut

                # Définition de l'emplacement fixe des brouillons
                if t < 4:
                    ty = 0
                elif t > 6:
                    ty = 6
                else:
                    ty = 3

                if t % 3 == 1 or t == 1:
                    tx = 2
                elif t % 3 == 2 or t == 2:
                    tx = 11
                else:
                    tx = 21

                window.blit(text, (x + 2 * tx, y + 6 * ty))

        elif not (self.getValue() == 0): # Valeur
            text = fnt.render(str(self.getValue()), 1, value_color) # Couleur des valeurs selon la variable color
            window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        # Mise en évidence de la case sélectionnée
        if self.selected:
            pygame.draw.rect(window, selected_color, (x, y, gap, gap), 3)
