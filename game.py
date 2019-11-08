import Sudoku
from Sudoku import *

import Timer
from Timer import *

import grids
from grids import *

import grids_soluce
from grids_soluce import *


def create_grid(size, grid_tab):
    coords = []
    squares = []
    for i in range(0, size):
        for j in range(0, size):
            coords.append(Coordinates(i, j))

    for i in range(0, len(coords)):
        squares.append(Square(coords[i], grid_tab[i], [], grid_tab[i] != 0, grid_tab[i] != 0))

    return squares


def chooseSquare(grid):
    x = 0
    y = 0
    while x < 1 or x > 9:
        x = int(input("Sur quelle ligne se trouve la case choisie ? "))
    while y < 1 or y > 9:
        y = int(input("Sur quelle colonne se trouve la case choisie ? "))
    return grid.getSquare(Coordinates(x, y).fromCoordinatesToNumber(grid.size()))


def clue(grid):
    checked = grid.listOfSquaresByChecked(True)
    unchecked = grid.listOfSquaresByChecked(False)
    print("Les cases suivantes sont correctes :")
    for c in checked:
        c.afficher()
    print("Les cases suivantes sont incorrectes :")
    for u in unchecked:
        u.afficher()


def winOrLoose(counter, max, grid):
    if counter > max:
        return True
    else:
        return grid.complete_checked()


quit = False
choice1 = 'M'
name = None
size = 9
error_counter = 0
sudoku = None

while quit is False:

    if choice1 == 'J':
        name = input("Entrez votre nom :")
        level = int(input("Entrez le niveau auquel vous souhaitez jouer :"))

        if level < 1:
            level = 1
        elif level > 3:
            level = 3

        grid = Grid(level, create_grid(size, grid_empty[level - 1]))
        sudoku = Sudoku(grid)

        sudoku.afficher()
        end = False
        choice2 = 'L'

        while end is False:

            if choice2 == 'V':
                s = chooseSquare(sudoku.getGrid())

                if s.isFixed():
                    print("Tu ne peux pas modifier cette case.")
                else:
                    v = 0
                    while v < 1 or v > 9:
                        v = int(input("Quelle valeur voulez-vous renseigner ? "))
                    sudoku.addValue(s, v)
                    sudoku.clearTrials(s)

                    if grid_soluce[level - 1][s.getCoordinates().fromCoordinatesToNumber(size)] == v:
                        s.setChecked(True)
                    else:
                        s.setChecked(False)
                        if level == 3:
                            error_counter += 1

                    if level == 3:
                        end = winOrLoose(error_counter, 3, sudoku.getGrid())
                    else:
                        end = sudoku.getGrid().complete_checked()
                    sudoku.afficher()
                    choice2 = 'L'

            elif choice2 == 'B':
                s = chooseSquare(sudoku.getGrid())

                if s.isFixed():
                    print("Tu ne peux pas modifier cette case.")
                elif s.getValue() != '0':
                    print("Attention, pour entrer un brouillon dans une case, il faut d'abord que tu la vides.")
                else:
                    t = 0
                    while t < 1 or t > 9:
                        t = int(input("Quelle valeur voulez-vous renseigner pour votre brouillon ? "))
                    sudoku.addTrial(s, t)
                    sudoku.afficher()
                    choice2 = 'L'
            elif choice2 == 'Z':
                s = chooseSquare(sudoku.getGrid())
                sudoku.clearSquare(s)
                s.setChecked(False)
                sudoku.afficher()
                choice2 = 'L'
            elif choice2 == 'E':
                s = chooseSquare(sudoku.getGrid())
                t = 0
                while t < 1 or t > 9:
                    t = int(input("Quelle valeur voulez-vous effacer de votre brouillon ? "))
                sudoku.removeTrial(s, t)
                sudoku.afficher()
                choice2 = 'L'
            elif choice2 == 'I':
                if level == 1:
                    clue(sudoku.getGrid())
                else:
                    print("Petit malin...")
                choice2 = 'L'
            elif choice2 == 'L':
                print('_____________________________')
                print('(V) - Entrer une valeur')
                print('(B) - Entrer un brouillon')
                print('(Z) - Effacer une case')
                print('(E) - Effacer un brouillon')
                if level == 1:
                    print(('(I) - Indice'))
                print('(M) - Revenir au menu')
                print('_____________________________')
                choice2 = input()
            elif choice2 == 'M':
                print('Attention, toutes vos modifications seront perdues. Souhaitez-vous continuer ?')
                print('(V) - Valider')
                print('Toute autre action annulera votre démarche.')
                ok = input()

                if ok == 'V':
                    choice1 = 'M'
                    end = True
                else:
                    choice2 = 'L'
            else:
                print('Veuillez vérifier votre réponse, elle ne correspond à aucune action connue.')
                choice2 = 'L'

        choice1 = 'E'
    elif choice1 == 'C':
        print(
            "Remplissez les cases avec un chiffre de 1 à 9. Attention à n'utiliser un chiffre qu'une seule fois par ligne, par colonne et par carré. Vous pouvez choisir votre niveau de jeu, de 1 à 3. Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non. Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur. Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.")
        print("Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non.")
        print("Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur.")
        print("Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.")
        print('_____________________________')
        print('(M) - Menu')
        print('(Q) - Quitter')
        print('_____________________________')
        choice1 = input()
    elif choice1 == 'M':
        print('_____________________________')
        print('(J) - Jouer')
        print('(C) - Crédits')
        print('(Q) - Quitter')
        print('_____________________________')
        choice1 = input()
    elif choice1 == 'E':
        if sudoku.getGrid().complete_checked():
            print('Bravo {} ! Vous avez terminé la grille avec succès !'.format(name))
        elif not sudoku.getGrid().complete_checked():
            print('Oh... Désolé, {}, mais tu as perdu.'.format(name))
        else:
            print('Petit malin...')
        choice1 = 'M'
    elif choice1 == 'Q':
        quit = True
    else:
        print('Veuillez vérifier votre réponse, elle ne correspond à aucune action connue.')
        choice1 = 'M'
