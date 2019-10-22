"""Classe Square (case)
Auteur : Charlotte Dujardin
Date : 22 octobre 2019"""

# Imports
import Coordinates
from Coordinates import *

class Square():
    def __init__(self, coordinates, value = 0, trials = [], checked = False):
        self.coordinates = coordinates
        self.value = value
        self.trials = trials
        self.checked = checked

    def getCoordinates(self):
        return self.coordinates

    def setCoordinates(self, new_coordinates):
        self.coordinates = new_coordinates

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value

    def getTrials(self):
        return self.trials

    def getTrial(self, n):
        return self.trials[n]

    def addTrial(self, new_trial):
        self.trials.append(new_trial)

    def isChecked(self):
        return self.checked

    def setChecked(self, new_checked):
        self.checked = new_checked

    def clearValue(self):
        self.setValue(0)

    def clearTrials(self):
        self.getTrials().clear()

    def clearTrial(self, trial):
        self.getTrials().remove(trial)
