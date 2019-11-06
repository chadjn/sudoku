import Column
from Column import *

import Coordinates
from Coordinates import *

import Grid
from Grid import *

import Level
from Level import *

import Line
from Line import *

import Piece
from Piece import *

import Player
from Player import *

import Square
from Square import *

import Sudoku
from Sudoku import *

import Timer
from Timer import *

import grids
from grids import *

quit = False
choice1 = 'M'

coords = []
squares = []
for i in range(0, 9):
    for j in range(0, 9):
        coords.append(Coordinates(i, j))

for i in range(0, len(coords)):
    squares.append(Square(coords[i], 0, [], True))

while quit != True :

    if choice1 == 'J' :
        name = input("Entrez votre nom :")
        player = Player(name)

        level_choice = int(input("Entrez le niveau auquel vous souhaitez jouer :"))

        if level_choice < 1 :
            level = Level(1)
        elif level_choice > 3 :
            level = Level(3)
        else :
            level = Level(level_choice)

        for i in range(0, len(squares)):
            squares[i].setValue(grid_empty[level.getNumber() - 1][i])
            if grid_empty[level.getNumber() - 1][i] == 0:
                squares[i].setChecked(False)

        grid = Grid(level.getNumber(), squares)
        sudoku = Sudoku(grid)

        sudoku.afficher()
        menu = False

        while menu != True :
            print('_____________________________')
            print('(C) - Entrer un chiffre')
            print('(B) - Entrer un brouillon')
            print('(Z) - Effacer une case')
            print('(E) - Effacer un brouillon')
            print('(M) - Revenir au menu')
            print('_____________________________')
            choice2 = input()

            if choice2 == 'C' :
                sx = int(input("Sur quelle ligne se trouve la case que vous voulez remplir ? "))
                sy = int(input("Sur quelle colonne se trouve la case que vous voulez remplir ? "))
                s = sudoku.getGrid().getSquare((sx - 1) * 9 + (sy - 1))
                v = int(input("Quelle valeur voulez-vous renseigner ? "))
                sudoku.addValue(s, v)
                sudoku.afficher()
            elif choice2 == 'B' :
                sx = int(input("Sur quelle ligne se trouve la case dont vous voulez renseigner un brouillon ? "))
                sy = int(input("Sur quelle colonne se trouve la case dont vous voulez renseigner un brouillon ? "))
                s = sudoku.getGrid().getSquare((sx - 1) * 9 + (sy - 1))
                t = int(input("Quelle valeur voulez-vous renseigner pour votre brouillon ? "))
                sudoku.addTrial(s, t)
                sudoku.afficher()
            elif choice2 == 'Z' :
                sx = int(input("Sur quelle ligne se trouve la case que vous voulez effacer ? "))
                sy = int(input("Sur quelle colonne se trouve la case que vous voulez effacer ? "))
                s = sudoku.getGrid().getSquare((sx - 1) * 9 + (sy - 1))
                sudoku.clearSquare(s)
                sudoku.afficher()
            elif choice2 == 'E' :
                sx = int(input("Sur quelle ligne se trouve la case dont vous voulez effacer un brouillon ? "))
                sy = int(input("Sur quelle colonne se trouve la case dont vous voulez effacer un brouillon ? "))
                s = sudoku.getGrid().getSquare((sx - 1) * 9 + (sy - 1))
                t = int(input("Quelle valeur voulez-vous effacer de votre brouillon ? "))
                sudoku.removeTrial(s, t)
                sudoku.afficher()
            elif choice2 == 'M' :
                menu = True
                choice1 = 'M'
            else :
                print('Veuillez vérifier votre réponse, elle ne correspond à aucune action connue.')
    elif choice1 == 'C' :
        print("Remplissez les cases avec un chiffre de 1 à 9. Attention à n'utiliser un chiffre qu'une seule fois par ligne, par colonne et par carré. Vous pouvez choisir votre niveau de jeu, de 1 à 3. Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non. Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur. Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.")
        print("Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non.")
        print("Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur.")
        print("Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.")
        print('_____________________________')
        print('(M) - Menu')
        print('(Q) - Quitter')
        print('_____________________________')
        choice1 = input()
    elif choice1 == 'M' :
        print('_____________________________')
        print('(J) - Jouer')
        print('(C) - Crédits')
        print('(Q) - Quitter')
        print('_____________________________')
        choice1 = input()
    elif choice1 == 'Q':
        quit = True
    else :
        print('Veuillez vérifier votre réponse, elle ne correspond à aucune action connue.')


