"""
Mardi 22 octobre 2019
Lucille Gueguen et Léa Dollé
"""

#classe servant au carré de 9 cases/cellules
import pygame

import Coordinates
from Coordinates import *

class Square :

    def __init__ (self, width, height, coordinates, value=0, trials=[], fixed = False, checked=False) :
        self.width = width
        self.height = height
        self.selected = False

        self.value = value
        self.trials = trials
        self.fixed = fixed
        self.checked = checked
        self.coordinates = coordinates

    def getWidth (self) :
        return self.width

    def setWidth (self, new_width) :
        self.width = new_width

    def getHeight (self) :
        return self.height

    def setHeight (self, new_height) :
        self.height = new_height

    def isSelected(self):
        return self.selected

    def setSelected(self, new_selected):
        self.selected = new_selected

    def getValue (self) :
        return self.value

    def setValue (self, new_value) :
        self.value = new_value

    def getTrials (self):
        return self.trials

    def getTrial (self, n):
        return self.trials[n] #accéder à un indice tu tableau

    def haveTrial(self, n):
        return any(t == n for t in self.trials) #vérifier que la donnée existe

    def addTrial (self, new_trial) :
        self.trials.append(new_trial)

    def isFixed(self):
        return self.fixed

    def setFixed(self, new_fixed):
        self.fixed = new_fixed

    def isChecked (self):
        return self.checked

    def setChecked (self, new_checked):
        self.checked = new_checked

    def getCoordinates (self):
        return self.coordinates

    def setCoordinates (self, new_coordinates) :
        self.coordinates = new_coordinates

    def clearTrial (self, trial) :
        self.trials.remove (trial)

    def clearTrials (self) :
        self.trials.clear ()

    def clearValue (self):
        self.value = 0

    def afficher(self, end):
        print(str(self.getValue()) + " ", end=end)

    def afficher_trials(self, line, end, fill):
        print('[{}][{}][{}] '.format(3*line-2 if self.haveTrial(3*line-2) else fill,
                                     3*line-1 if self.haveTrial(3*line-1) else fill,
                                     3*line if self.haveTrial(3*line) else fill), end=end)

    def drawSquare(self, window):
        fnt = pygame.font.SysFont("Arial", 20)

        gap = self.width / 9
        x = self.getCoordinates().getY() * gap
        y = self.getCoordinates().getX() * gap

        if self.getTrials() != [] and self.getValue() == 0:
            text = fnt.render(str(self.getTrials()), 1, (128, 128, 128))
            window.blit(text, (x + 5, y + 5))
        elif not (self.getValue() == 0):
            text = fnt.render(str(self.getValue()), 1, (0, 0, 0))
            window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(window, (255, 0, 0), (x, y, gap, gap), 3)
