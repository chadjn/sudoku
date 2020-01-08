"""Script d'interface
Auteur : Charlotte Dujardin
Date : 28 décembre 2019"""

import pygame
from pygame.locals import *
import os
import traceback # récupération des informations sur les erreurs

from game import winOrLoose

import Sudoku
from Sudoku import *

import grids
from grids import *

import grids_soluce
from grids_soluce import *

pygame.font.init()

try:
    os.environ['SDL_VIDEO_WINDOW_POS']="100,100"

    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Sudoku ChaLuLé")

    def redrawWindow(win, board, level, clue):
        win.fill((255, 255, 255))
        if level == 1:
            text = fnt_span.render("(I) - Indices", 1, (0, 0, 0))
            fenetre.blit(text, (500, 400))
        text = fnt_span.render("(R) - Reset", 1, (0, 0, 0))
        fenetre.blit(text, (500, 420))
        text = fnt_span.render("(M) - Menu", 1, (0, 0, 0))
        fenetre.blit(text, (500, 440))
        board.drawGrid(win, clue)

    def insertNumber(key):
        if key == pygame.K_1 or key == pygame.K_KP1:
            return 1
        if key == pygame.K_2 or key == pygame.K_KP2:
            return 2
        if key == pygame.K_3 or key == pygame.K_KP3:
            return 3
        if key == pygame.K_4 or key == pygame.K_KP4:
            return 4
        if key == pygame.K_5 or key == pygame.K_KP5:
            return 5
        if key == pygame.K_6 or key == pygame.K_KP6:
            return 6
        if key == pygame.K_7 or key == pygame.K_KP7:
            return 7
        if key == pygame.K_8 or key == pygame.K_KP8:
            return 8
        if key == pygame.K_9 or key == pygame.K_KP9:
            return 9

    # BOUCLE INFINIE
    key = None
    run = True
    size = 9

    while run:
        # Création de l'arrière-plan
        menu_bg = pygame.Surface(fenetre.get_size())
        menu_bg = menu_bg.convert()
        menu_bg.fill((255, 255, 255))

        # Affichage du menu
        fnt_h1 = pygame.font.Font('C:\WINDOWS\FONTS\CARYBE_0.OTF', 50)
        fnt_h2 = pygame.font.Font('C:\WINDOWS\FONTS\CARYBE_0.OTF', 30)
        fnt_span = pygame.font.Font('C:\WINDOWS\FONTS\CARYBE_0.OTF', 16)
        fnt_p = pygame.font.SysFont("Arial", 16)

        text = fnt_h1.render("Sudoku", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        menu_bg.blit(text, textpos)

        text = fnt_h2.render("(J) - Jouer", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 200
        menu_bg.blit(text, textpos)
        text = fnt_h2.render("(R) - Règlement", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 250
        menu_bg.blit(text, textpos)
        text = fnt_h2.render("(Q) - Quitter", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 300
        menu_bg.blit(text, textpos)

        fenetre.blit(menu_bg, (0,0))

        # Rafraichissement
        pygame.display.flip()

        menu = True
        rules = True
        form = True
        play = True
        warning = True
        clue = True
        remove = True

        while menu:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_a:
                    menu = False
                    rules = False
                    form = False
                    play = False
                    warning = False
                    clue = False
                    remove = False
                    run = False
                    choice = None
                elif event.type == KEYDOWN:
                    if event.key == K_j:
                        menu = False
                        rules = False
                        form = True
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        choice = 'J'
                    elif event.key == K_r:
                        menu = False
                        rules = True
                        form = False
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        choice = 'R'

        if choice == 'R':
            # Création de l'arrière-plan
            rules_bg = pygame.Surface(fenetre.get_size())
            rules_bg = rules_bg.convert()
            rules_bg.fill((255, 255, 255))

            text = fnt_h2.render("Règlement", 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            rules_bg.blit(text, textpos)

            text = fnt_p.render("Remplissez les cases avec un chiffre de 1 à 9. Attention à n'utiliser un chiffre qu'une seule fois", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 100))
            text = fnt_p.render("par ligne, par colonne et par carré. Vous pouvez choisir votre niveau de jeu, de 1 à 3.", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 120))
            text = fnt_p.render("Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non.", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 140))
            text = fnt_p.render("Le deuxième niveau n'a pas d'indices mais n'a pas non plus de système d'erreur.", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 160))
            text = fnt_p.render("Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 180))

            text = fnt_span.render("(J) - Jouer", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 380))
            text = fnt_span.render("(M) - Menu", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 400))
            text = fnt_span.render("(Q) - Quitter", 1, (0, 0, 0))
            rules_bg.blit(text, (20, 420))

            fenetre.blit(rules_bg, (0,0))

            pygame.display.flip()

            while rules:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        form = False
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        run = False
                        choice = None
                    elif event.type == KEYDOWN:
                        if event.key == K_j:
                            menu = False
                            rules = False
                            form = True
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'J'
                        elif event.key == K_SEMICOLON:
                            menu = True
                            rules = False
                            form = False
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'M'

        elif choice == 'J':
            # Création de l'arrière-plan
            form_bg = pygame.Surface(fenetre.get_size())
            form_bg = form_bg.convert()
            form_bg.fill((255, 255, 255))

            text = fnt_h2.render("Jouer", 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            form_bg.blit(text, textpos)

            text = fnt_span.render("(F1) - Jouer au niveau 1", 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 200
            form_bg.blit(text, textpos)
            text = fnt_span.render("(F2) - Jouer au niveau 2", 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 230
            form_bg.blit(text, textpos)
            text = fnt_span.render("(F3) - Jouer au niveau 3", 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 260
            form_bg.blit(text, textpos)

            fenetre.blit(form_bg, (0, 0))

            pygame.display.flip()

            while form:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        form = False
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        run = False
                        level = None
                    elif event.type == KEYDOWN:
                        if event.key == K_F1:
                            menu = False
                            rules = False
                            form = False
                            play = True
                            warning = False
                            clue = False
                            remove = False
                            level = 1
                        elif event.key == K_F2:
                            menu = False
                            rules = False
                            form = False
                            play = True
                            warning = False
                            clue = False
                            remove = False
                            level = 2
                        elif event.key == K_F3:
                            menu = False
                            rules = False
                            form = False
                            play = True
                            warning = False
                            clue = False
                            remove = False
                            level = 3

            grid = Grid(level, size, 480, 480, grid_empty[level - 1])
            sudoku = Sudoku(grid)
            error_counter = 0

            while play:
                end = False
                for event in pygame.event.get():  # Attente des événements
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        form = False
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        run = False
                    if event.type == pygame.KEYDOWN:
                        key = insertNumber(event.key)
                        if event.key == pygame.K_RETURN:
                            menu = True
                            rules = False
                            form = False
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'M'
                        if event.key == pygame.K_SEMICOLON:
                            warning = True
                            key = 'M'
                        if event.key == pygame.K_i:
                            clue = True
                            key = 'I'
                        if event.key == pygame.K_r:
                            key = 'R'
                        if event.key == pygame.K_BACKSPACE:
                            remove = True
                            key = "B"
                        if event.key == pygame.K_DELETE:
                            key = "D"
                        if event.key == pygame.K_ESCAPE:
                            key = "E"
                        if event.key == pygame.K_DOWN:
                            sudoku.getGrid().setSketching(True)
                        if event.key == pygame.K_UP:
                            sudoku.getGrid().setSketching(False)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        clicked = sudoku.click(pos)
                        if clicked:
                            sudoku.select(clicked)
                            key = None

                    if key == 'M':
                        # Création de l'arrière-plan
                        warning_bg = pygame.Surface((440, 160))
                        warning_bg = warning_bg.convert()
                        warning_bg.fill((255, 255, 255))

                        text = fnt_span.render("Attention", 1, (0, 0, 0))
                        textpos = text.get_rect()
                        textpos.centerx = fenetre.get_rect().centerx
                        textpos.y = 20
                        warning_bg.blit(text, textpos)
                        text = fnt_p.render("Toutes vos modifications seront perdues. Souhaitez-vous continuer ?", 1, (0, 0, 0))
                        warning_bg.blit(text, (20, 60))
                        text = fnt_p.render("(V) - Valider", 1, (0, 0, 0))
                        warning_bg.blit(text, (20, 100))
                        text = fnt_p.render("Toute autre action annulera votre démarche.", 1, (0, 0, 0))
                        warning_bg.blit(text, (20, 120))

                        fenetre.blit(warning_bg, (100, 160))

                        pygame.display.flip()

                        while warning:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                                    menu = False
                                    rules = False
                                    form = False
                                    play = False
                                    warning = False
                                    clue = False
                                    remove = False
                                    run = False
                                if event.type == KEYDOWN:
                                    if event.key == K_v:
                                        menu = True
                                        rules = False
                                        form = False
                                        play = False
                                        warning = False
                                        clue = False
                                        remove = False
                                        choice = 'M'
                                    else:
                                        warning = False
                        key = None
                    elif key == 'I':
                        redrawWindow(fenetre, sudoku.getGrid(), level, True)
                        pygame.display.update()
                        while clue:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                                    menu = False
                                    rules = False
                                    form = False
                                    play = False
                                    warning = False
                                    clue = False
                                    remove = False
                                    run = False
                                if event.type == KEYDOWN:
                                    if event.key == K_i:
                                        pygame.display.update()
                                        clue = False
                        key = None
                    elif key == 'R':
                        for i in range(size):
                            for j in range(size):
                                s = sudoku.getGrid().getSquare(i,j)
                                if not s.isFixed():
                                    sudoku.clearSquare(s)
                        key = None

                    if level == 3:
                        end = winOrLoose(error_counter, 3, sudoku.getGrid())
                    else:
                        end = sudoku.getGrid().complete_checked()

                    if not end:
                        if sudoku.getGrid().getSelected() and key != None:
                            coord = sudoku.getGrid().getSelected()
                            selected_square = sudoku.getGrid().getSquare(coord.getX(), coord.getY())

                            if not selected_square.isFixed():
                                if key == "E":
                                    sudoku.clearSquare(selected_square)
                                elif key == "D":
                                    sudoku.clearTrials(selected_square)
                                elif key == "B":
                                    while remove:
                                        for event in pygame.event.get():
                                            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                                                menu = False
                                                rules = False
                                                form = False
                                                play = False
                                                warning = False
                                                clue = False
                                                remove = False
                                                run = False
                                            if event.type == KEYDOWN:
                                                key = insertNumber(event.key)
                                                remove = False
                                    sudoku.removeTrial(selected_square, key)
                                else :
                                    if sudoku.getGrid().isSketching():
                                        if selected_square.getValue() == 0:
                                            sudoku.addTrial(selected_square, key)
                                        sudoku.getGrid().setSketching(False)
                                    else:
                                        sudoku.addValue(selected_square, key)
                                        sudoku.clearTrials(selected_square)

                                        # Si la valeur renseignée correspond à celle entrée dans les solutions, alors l'attribut checked passe à True (pour signifier que la valeur est correcte)
                                        if grid_soluce[level - 1][selected_square.getCoordinates().fromCoordinatesToNumber(9)] == key:
                                            selected_square.setChecked(True)
                                        # Sinon la case est considérée comme incorrecte (cas où la valeur est modifiée même remplaçant une valeur correcte)
                                        else:
                                            selected_square.setChecked(False)

                                            if level == 3:
                                                error_counter += 1

                        redrawWindow(fenetre, sudoku.getGrid(), level, False)
                        pygame.display.update()
                        key = None
                    else:
                        # Création de l'arrière-plan
                        end_bg = pygame.Surface(fenetre.get_size())
                        end_bg = end_bg.convert()
                        end_bg.fill((255, 255, 255))

                        if sudoku.getGrid().complete_checked():
                            text = fnt_h2.render("Bravo !", 1, (0, 0, 0))
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 150
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("Vous avez terminé", 1, (0, 0, 0))
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 200
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("la grille avec succès !", 1, (0, 0, 0))
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 250
                            end_bg.blit(text, textpos)

                        else:
                            text = fnt_h2.render("Oh... Quelle tristesse !", 1, (0, 0, 0))
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 150
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("Vous avez perdu.", 1, (0, 0, 0))
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 200
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("Retentez votre chance.", 1, (0, 0, 0))
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 250
                            end_bg.blit(text, textpos)

                        text = fnt_p.render("Appuyer sur la touche 'Entrée' pour revenir au menu.", 1, (0, 0, 0))
                        textpos = text.get_rect()
                        textpos.centerx = fenetre.get_rect().centerx
                        textpos.y = 400
                        end_bg.blit(text, textpos)

                        fenetre.blit(end_bg, (0, 0))

                        pygame.display.flip()

except:
    traceback.print_exc()

finally:
    pygame.quit()
    exit()