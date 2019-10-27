"""
Mardi 22 octobre 2019
Lucille Gueguen
"""

# classe mettant en place le timer du SUDOKU
class Timer:

    def __init__(self, secondes=0, minutes=0):
        self.secondes = secondes
        self.minutes = minutes

    def getSecondes(self):
        return self.secondes

    def setSecondes(self, new_secondes):
        self.secondes = new_secondes

    def getMinutes(self):
        return self.minutes

    def setMinutes(self, new_minutes):
        self.minutes = new_minutes

    def start(self):
        # Définition temporaire en attente d'un vrai timer --> TODO: timer dynamique ?
        self.secondes += 1
        print('START')

    def pause(self):
        # Définition temporaire en attente d'un vrai timer --> TODO: timer dynamique ?
        print('STOP')

    def reset(self):
        self.pause()
        self.setSecondes(0)
        self.setMinutes(0)
        print('RESET')


    def afficher(self):
        print("Timer : {}:{}".format(self.getMinutes(), self.getSecondes()))