"""Script principal
Auteur : Charlotte Dujardin
Date : 8 novembre 2019"""

import Sudoku
from Sudoku import *

import grids
from grids import *

import grids_soluce
from grids_soluce import *


# Fonction qui crée et remplit une grille
def create_grid(size, grid_tab):
    coords = []
    squares = []
    for i in range(0, size):
        for j in range(0, size):
            coords.append(Coordinates(i, j))

    for i in range(0, len(coords)):
        squares.append(Square(coords[i], grid_tab[i], [], grid_tab[i] != 0, grid_tab[i] != 0))

    return squares


# Fonction qui permet à l'utilisateur de renseigner la case avec laquelle il souhaite interagir
def chooseSquare(grid, size):
    x = 0
    y = 0
    while x < 1 or x > 9:
        x = int(input("Sur quelle ligne se trouve la case choisie ? "))
    while y < 1 or y > 9:
        y = int(input("Sur quelle colonne se trouve la case choisie ? "))
    return grid.getSquare(Coordinates(x, y).fromCoordinatesToNumber(size))


# Fonction qui renseigne quelles cases remplies par l'utilisateur sont correctes et lesquelles sont incorrectes
def clue(grid):
    checked = grid.listOfSquaresByChecked(True)
    unchecked = grid.listOfSquaresByChecked(False)
    print("Les cases suivantes sont correctes :")
    for c in checked:
        c.afficher()
    print("Les cases suivantes sont incorrectes :")
    for u in unchecked:
        u.afficher()


# Fonction qui vérifie si l'utilisateur a gagné ou perdu (rempli correctement, fait trop d'erreur ou a abandonné avant la fin)
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

# Tant que l'utlisateur n'a pas explicitement décidé de quitter le jeu, il peut interagir avec
while quit is False:

    # Accès au menu principal
    if choice1 == 'M':
        print('_____________________________')
        print('(J) - Jouer')
        print('(R) - Règlement')
        print('(Q) - Quitter')
        print('_____________________________')
        choice1 = input()

    # Quand l'utilisateur a décidé de jouer
    elif choice1 == 'J':

        name = input("Entrez votre nom :")
        level = int(input("Entrez le niveau auquel vous souhaitez jouer :"))

        # Si l'utilisateur choisit un niveau en dehors de ceux proposés, on le ramène aux niveaux les plus proches
        if level < 1:
            level = 1
        elif level > 3:
            level = 3

        grid = Grid(level, create_grid(size, grid_empty[level - 1]))
        sudoku = Sudoku(grid)

        sudoku.afficher()

        end = False
        choice2 = 'L'

        # Tant que le jeu n'est pas terminé (gagné, perdu ou abandonné), l'utilisateur peut interagir avec
        while end is False:

            # Menu intermédiaire d'interaction avec la grille
            if choice2 == 'L':
                print('_____________________________')
                print('(V) - Entrer une valeur')
                print('(B) - Entrer un brouillon')
                print('(Z) - Effacer une case')
                print('(E) - Effacer un brouillon')

                # Indices disponibles seulement au premier niveau
                if level == 1:
                    print(('(I) - Indice'))

                print('(M) - Revenir au menu')
                print('_____________________________')
                choice2 = input()

            # Entrer une valeur dans une case
            elif choice2 == 'V':
                s = chooseSquare(sudoku.getGrid())

                # Si la case est fixe, elle n'est pas modifiable
                if s.isFixed():
                    print("Tu ne peux pas modifier cette case.")
                else:
                    v = 0
                    while v < 1 or v > 9:
                        v = int(input("Quelle valeur voulez-vous renseigner ? "))
                    sudoku.addValue(s, v)
                    sudoku.clearTrials(s)

                    # Si la valeur renseignée correspond à celle entrée dans les solutions, alors l'attribut checked passe à True (pour signifier que la valeur est correcte)
                    if grid_soluce[level - 1][s.getCoordinates().fromCoordinatesToNumber(size)] == v:
                        s.setChecked(True)
                    # Sinon la case est considérée comme incorrecte (cas où la valeur est modifiée même remplaçant une valeur correcte)
                    else:
                        s.setChecked(False)

                        # Si le niveau est le niveau 3, alors chaque valeur incorrecte est comptabilisée
                        if level == 3:
                            error_counter += 1

                    # Si le niveau est le niveau 3, on vérifie que l'utilisateur gagne ou perd
                    if level == 3:
                        end = winOrLoose(error_counter, 3, sudoku.getGrid())

                    # Sinon, on vérifie que le sudoku est complet et correct
                    else:
                        end = sudoku.getGrid().complete_checked()

                    sudoku.afficher()

                    # On retourne ensuite au menu intermédiaire
                    choice2 = 'L'

            # Entrer un brouillon dans une case
            elif choice2 == 'B':
                s = chooseSquare(sudoku.getGrid())

                # Si la case est fixe, elle n'est pas modifiable
                if s.isFixed():
                    print("Tu ne peux pas modifier cette case.")

                # Si la case n'est pas vide, elle ne peut pas recevoir de brouillon
                elif s.getValue() != 0:
                    print("Attention, pour entrer un brouillon dans une case, il faut d'abord que tu la vides.")
                else:
                    t = 0
                    while t < 1 or t > 9:
                        t = int(input("Quelle valeur voulez-vous renseigner pour votre brouillon ? "))
                    sudoku.addTrial(s, t)
                    sudoku.afficher()

                    # On retourne ensuite au menu intermédiaire
                    choice2 = 'L'

            # Effacer une case
            elif choice2 == 'Z':
                s = chooseSquare(sudoku.getGrid())
                sudoku.clearSquare(s)
                s.setChecked(False)
                sudoku.afficher()

                # On retourne ensuite au menu intermédiaire
                choice2 = 'L'

            # Effacer un brouillon
            elif choice2 == 'E':
                s = chooseSquare(sudoku.getGrid())
                t = 0
                while t < 1 or t > 9:
                    t = int(input("Quelle valeur voulez-vous effacer de votre brouillon ? "))
                sudoku.removeTrial(s, t)
                sudoku.afficher()

                # On retourne ensuite au menu intermédiaire
                choice2 = 'L'

            # Accéder aux indices
            elif choice2 == 'I':

                # Si le niveau n'est pas le niveau 1, on affiche un message d'erreur
                if level == 1:
                    clue(sudoku.getGrid())
                else:
                    print("Petit malin...")

                # On retourne ensuite au menu intermédiaire
                choice2 = 'L'

            # Retourner au menu
            elif choice2 == 'M':

                # Étant donné qu'il s'agit également d'une remise à zéro, on s'assure qu'il s'agit bien du choix de l'utilisateur
                print('Attention, toutes vos modifications seront perdues. Souhaitez-vous continuer ?')
                print('(V) - Valider')
                print('Toute autre action annulera votre démarche.')
                ok = input()

                if ok == 'V':
                    choice1 = 'M'
                    end = True
                else:
                    choice2 = 'L'

            # Toute autre action de l'utilisateur le mène vers un message d'erreur
            else:
                print('Veuillez vérifier votre réponse, elle ne correspond à aucune action connue.')
                choice2 = 'L'

        choice1 = 'E'

    # Voir le règlement
    elif choice1 == 'R':
        print("Remplissez les cases avec un chiffre de 1 à 9. Attention à n'utiliser un chiffre qu'une seule fois par ligne, par colonne et par carré. Vous pouvez choisir votre niveau de jeu, de 1 à 3. Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non. Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur. Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.")
        print("Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non.")
        print("Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur.")
        print("Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.")
        print('_____________________________')
        print('(M) - Menu')
        print('(Q) - Quitter')
        print('_____________________________')
        choice1 = input()

    # Écran de fin de jeu
    elif choice1 == 'E':

        # Si le sudoku est complet et correct, alors un message de réussite s'affiche
        if sudoku.getGrid().complete_checked():
            print('Bravo {} ! Vous avez terminé la grille avec succès !'.format(name))

        # Si le sudoku est incomplet et/ou incorrect, alors un message de défaite s'affiche
        elif not sudoku.getGrid().complete_checked():
            print('Oh... Désolé, {}, mais tu as perdu.'.format(name))

        # Sinon, c'est un utilisage détourné, nous le faisons remarquer
        else:
            print('Petit malin...')

        # On retourne ensuite au menu principal
        choice1 = 'M'

    # Quitter le jeu
    elif choice1 == 'Q':
        quit = True

    # Toute autre action de l'utilisateur le mène vers un message d'erreur
    else:
        print('Veuillez vérifier votre réponse, elle ne correspond à aucune action connue.')

        # On retourne ensuite au menu principal
        choice1 = 'M'
