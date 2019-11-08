"""
Mardi 22 octobre 2019
Lucille Gueguen et Léa Dollé
"""

#classe servant au carré de 9 cases/cellules

import Coordinates
from Coordinates import *

class Square :

    def __init__ (self, coordinates, value=0, trials=[], fixed = False, checked=False) :
        self.value = value
        self.trials = trials
        self.fixed = fixed
        self.checked = checked
        self.coordinates = coordinates

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

    def afficher(self):
        print('[{}] (brouillon : {})'.format(self.getValue(), self.getTrials()))