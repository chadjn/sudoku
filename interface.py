"""Script d'interface
Auteur : Charlotte Dujardin
Date : 28 décembre 2019"""

import pygame
from pygame.locals import *
import os
import traceback  # Récupération des informations sur les erreurs

import Sudoku
from Sudoku import *

import grids
from grids import *

import grids_soluce
from grids_soluce import *

pygame.font.init()

try:
    # Affichage de la fenêtre de jeu à une position donnée
    os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"

    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Sudoku ChaLuLé")

    # Fonction qui met à jour la grille
    def redrawWindow(win, board, level, clue, bg_color, bg_side_color, line_color, selected_color, text_color, trial_color, checked_color, unchecked_color):
        win.fill(bg_color)

        div = pygame.Surface((160, fenetre.get_height()))
        div = div.convert()
        div.fill(bg_side_color)
        fenetre.blit(div, (480, 0))

        if level == 1:
            text = fnt_span.render("(A) - Aide", 1, text_color)
            fenetre.blit(text, (500, 400))
        text = fnt_span.render("(R) - Reset", 1, text_color)
        fenetre.blit(text, (500, 420))
        text = fnt_span.render("(M) - Menu", 1, text_color)

        fenetre.blit(text, (500, 440))
        board.drawGrid(win, clue, line_color, selected_color, text_color, trial_color, checked_color, unchecked_color)


    # Fonction qui renvoie le nombre sélectionné au clavier
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


    # Fonction qui vérifie si l'utilisateur a gagné ou perdu (rempli correctement, fait trop d'erreur ou a abandonné avant la fin)
    def winOrLoose(counter, max, grid):
        if counter > max:
            return True
        else:
            return grid.complete_checked()

    # Début de la boucle infinie
    key = None
    run = True
    size = 9

    while run:
        # Définition des polices
        fnt_h1 = pygame.font.Font('Carybe.otf', 50)
        fnt_h2 = pygame.font.Font('Carybe.otf', 30)
        fnt_span = pygame.font.Font('Carybe.otf', 16)
        fnt_p = pygame.font.SysFont("Arial", 16)

        # Définition des couleurs
        white_color = (255, 255, 255)
        dark_color = (47, 53, 56)
        grey_color = (130, 130, 130)
        light_blue_color = (212, 229, 244)
        average_blue_color = (27, 68, 105)
        dark_blue_color = (34, 51, 66)
        green_color = (150, 204, 80)
        red_color = (255, 60, 68)
        light_red_color = (244, 157, 180)

        # Création de l'arrière-plan
        menu_bg = pygame.Surface(fenetre.get_size())
        menu_bg = menu_bg.convert()
        menu_bg.fill(light_blue_color)

        # Affichage du titre
        text = fnt_h1.render("Sudoku", 1, dark_blue_color)
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 20
        menu_bg.blit(text, textpos)

        # Affichage du menu
        text = fnt_h2.render("(J) - Jouer", 1, dark_color)
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 180
        menu_bg.blit(text, textpos)
        text = fnt_h2.render("(R) - Règlement", 1, dark_color)
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 230
        menu_bg.blit(text, textpos)
        text = fnt_h2.render("(I) - Instructions de jeu", 1, dark_color)
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 280
        menu_bg.blit(text, textpos)
        text = fnt_h2.render("(Q) - Quitter", 1, dark_color)
        textpos = text.get_rect()
        textpos.centerx = fenetre.get_rect().centerx
        textpos.y = 330
        menu_bg.blit(text, textpos)

        fenetre.blit(menu_bg, (0, 0))

        # Rafraichissement
        pygame.display.flip()

        # Initialisation des boucles internes
        menu = True
        rules = True
        how_to = True
        form = True
        play = True
        warning = True
        clue = True
        remove = True

        # Boucle de menu principal
        while menu:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_a:
                    menu = False
                    rules = False
                    how_to = False
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
                        how_to = False
                        form = True
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        choice = 'J'
                    elif event.key == K_r:
                        menu = False
                        rules = True
                        how_to = False
                        form = False
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        choice = 'R'
                    elif event.key == K_i:
                        menu = False
                        rules = False
                        how_to = True
                        form = False
                        play = False
                        warning = False
                        clue = False
                        remove = False
                        choice = 'I'

        # Règlement
        if choice == 'R':
            # Création de l'arrière-plan
            rules_bg = pygame.Surface(fenetre.get_size())
            rules_bg = rules_bg.convert()
            rules_bg.fill((255, 255, 255))

            # Création de l'arrière-plan de titre
            rules_title = pygame.Surface((fenetre.get_width(), 80))
            rules_title = rules_title.convert()
            rules_title.fill(light_blue_color)

            # Affichage du titre
            text = fnt_h2.render("Règlement", 1, dark_blue_color)
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 20
            rules_title.blit(text, textpos)
            rules_bg.blit(rules_title, (0, 0))

            # Affichage du règlement
            text = fnt_p.render(
                "Remplissez les cases avec un chiffre de 1 à 9. Attention à n'utiliser un chiffre qu'une seule fois", 1,
                dark_color)
            rules_bg.blit(text, (20, 100))
            text = fnt_p.render(
                "par ligne, par colonne et par carré. Vous pouvez choisir votre niveau de jeu, de 1 à 3.", 1,
                dark_color)
            rules_bg.blit(text, (20, 120))
            text = fnt_p.render(
                "Le premier niveau fait apparaître les chiffres en vert ou en rouge, selon qu'il est correct ou non.",
                1, dark_color)
            rules_bg.blit(text, (20, 140))
            text = fnt_p.render("Le deuxième niveau n'a pas d'aide mais n'a pas non plus de système d'erreur.", 1,
                                dark_color)
            rules_bg.blit(text, (20, 160))
            text = fnt_p.render(
                "Le troisième et dernier niveau n'offre la possibilité de ne faire que trois erreurs maximum.", 1,
                dark_color)
            rules_bg.blit(text, (20, 180))

            # Affichage du menu
            text = fnt_span.render("(J) - Jouer", 1, dark_color)
            rules_bg.blit(text, (20, 380))
            text = fnt_span.render("(M) - Menu", 1, dark_color)
            rules_bg.blit(text, (20, 400))
            text = fnt_span.render("(Q) - Quitter", 1, dark_color)
            rules_bg.blit(text, (20, 420))

            fenetre.blit(rules_bg, (0, 0))

            pygame.display.flip()

            # Boucle règlement
            while rules:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        how_to = False
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
                            how_to = False
                            form = True
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'J'
                        elif event.key == K_SEMICOLON:
                            menu = True
                            rules = False
                            how_to = False
                            form = False
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'M'

        # Instructions de jeu
        if choice == 'I':
            # Création de l'arrière-plan
            how_to_bg = pygame.Surface(fenetre.get_size())
            how_to_bg = how_to_bg.convert()
            how_to_bg.fill((255, 255, 255))

            # Création de l'arrière-plan du titre
            how_to_title = pygame.Surface((fenetre.get_width(), 80))
            how_to_title = how_to_title.convert()
            how_to_title.fill(light_blue_color)

            # Affichage du titre
            text = fnt_h2.render("Instructions de jeu", 1, dark_blue_color)
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 20
            how_to_title.blit(text, textpos)
            how_to_bg.blit(how_to_title, (0, 0))

            # Affichage des instructions
            text = fnt_p.render("Pour choisir une case, sélectionnez-là avec le curseur.", 1, dark_color)
            how_to_bg.blit(text, (20, 100))
            text = fnt_p.render("Pour remplir une case, utilisez les chiffres de votre clavier.", 1, dark_color)
            how_to_bg.blit(text, (20, 120))
            text = fnt_p.render("Pour remplir un brouillon, appuyez sur la flèche du bas avant de sélectionner la valeur souhaitée.", 1, dark_color)
            how_to_bg.blit(text, (20, 140))
            text = fnt_p.render("Vous pouvez appuyez sur la flèche du haut pour annuler cette action (revenir au mode \"ajout de valeur\").", 1, dark_color)
            how_to_bg.blit(text, (20, 160))
            text = fnt_p.render("Pour effacer...", 1, dark_color)
            how_to_bg.blit(text, (20, 180))
            text = fnt_p.render("... la case entière : appuyez sur 'Échap' ;", 1, dark_color)
            how_to_bg.blit(text, (20, 200))
            text = fnt_p.render("... tous les brouillons d'une case : appuyez sur 'suppr' ;", 1, dark_color)
            how_to_bg.blit(text, (20, 220))
            text = fnt_p.render("... un brouillon particulier : appuyez sur 'Backspace' puis sur la valeur à effacer.", 1, dark_color)
            how_to_bg.blit(text, (20, 240))

            # Affichage du menu
            text = fnt_span.render("(J) - Jouer", 1, dark_color)
            how_to_bg.blit(text, (20, 380))
            text = fnt_span.render("(M) - Menu", 1, dark_color)
            how_to_bg.blit(text, (20, 400))
            text = fnt_span.render("(Q) - Quitter", 1, dark_color)
            how_to_bg.blit(text, (20, 420))

            fenetre.blit(how_to_bg, (0, 0))

            pygame.display.flip()

            # Boucle instructions
            while how_to:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        how_to = False
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
                            how_to = False
                            form = True
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'J'
                        elif event.key == K_SEMICOLON:
                            menu = True
                            rules = False
                            how_to = False
                            form = False
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'M'

        # Jouer
        if choice == 'J':
            # Création de l'arrière-plan
            form_bg = pygame.Surface(fenetre.get_size())
            form_bg = form_bg.convert()
            form_bg.fill((255, 255, 255))

            # Création de l'arrière-plan du titre
            form_title = pygame.Surface((fenetre.get_width(), 80))
            form_title = form_title.convert()
            form_title.fill(light_blue_color)

            # Affichage du titre
            text = fnt_h2.render("Jouer", 1, dark_blue_color)
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 20
            form_title.blit(text, textpos)
            form_bg.blit(form_title, (0, 0))

            # Affichage des niveaux
            text = fnt_span.render("(F1) - Jouer au niveau 1", 1, dark_color)
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 200
            form_bg.blit(text, textpos)
            text = fnt_span.render("(F2) - Jouer au niveau 2", 1, dark_color)
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 230
            form_bg.blit(text, textpos)
            text = fnt_span.render("(F3) - Jouer au niveau 3", 1, dark_color)
            textpos = text.get_rect()
            textpos.centerx = fenetre.get_rect().centerx
            textpos.y = 260
            form_bg.blit(text, textpos)

            fenetre.blit(form_bg, (0, 0))

            pygame.display.flip()

            # Boucle choix des niveaux
            while form:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        how_to = False
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
                            how_to = False
                            form = False
                            play = True
                            warning = False
                            clue = False
                            remove = False
                            level = 1
                        elif event.key == K_F2:
                            menu = False
                            rules = False
                            how_to = False
                            form = False
                            play = True
                            warning = False
                            clue = False
                            remove = False
                            level = 2
                        elif event.key == K_F3:
                            menu = False
                            rules = False
                            how_to = False
                            form = False
                            play = True
                            warning = False
                            clue = False
                            remove = False
                            level = 3

            grid = Grid(level, size, 480, 480, grid_empty[level - 1])
            sudoku = Sudoku(grid)
            error_counter = 0

            # Boucle jeu
            while play:
                end = False
                for event in pygame.event.get():  # Attente des événements
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        menu = False
                        rules = False
                        how_to = False
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
                            how_to = False
                            form = False
                            play = False
                            warning = False
                            clue = False
                            remove = False
                            choice = 'M'
                        if event.key == pygame.K_SEMICOLON:
                            warning = True
                            key = 'M'
                        if event.key == pygame.K_q:
                            clue = True
                            key = 'A'
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

                    # Affichage d'un message de prévention
                    if key == 'M':
                        # Création de l'arrière-plan
                        warning_bg = pygame.Surface((440, 160))
                        warning_bg = warning_bg.convert()
                        warning_bg.fill(light_red_color)

                        # Affichage du message
                        text = fnt_span.render("Attention", 1, dark_blue_color)
                        textpos = text.get_rect()
                        textpos.centerx = fenetre.get_rect().centerx
                        textpos.y = 20
                        warning_bg.blit(text, textpos)
                        text = fnt_p.render("Toutes vos modifications seront perdues. Souhaitez-vous continuer ?", 1, dark_color)
                        warning_bg.blit(text, (20, 60))
                        text = fnt_p.render("(V) - Valider", 1, dark_color)
                        warning_bg.blit(text, (20, 100))
                        text = fnt_p.render("Toute autre action annulera votre démarche.", 1, dark_color)
                        warning_bg.blit(text, (20, 120))

                        fenetre.blit(warning_bg, (100, 160))

                        pygame.display.flip()

                        # Boucle prévention
                        while warning:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                                    menu = False
                                    rules = False
                                    how_to = False
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
                                        how_to = False
                                        form = False
                                        play = False
                                        warning = False
                                        clue = False
                                        remove = False
                                        choice = 'M'
                                    else:
                                        warning = False
                        key = None

                    # Aide
                    elif key == 'A':
                        redrawWindow(fenetre, sudoku.getGrid(), level, True, white_color, light_blue_color, grey_color, average_blue_color, dark_color, grey_color, green_color, red_color)
                        pygame.display.update()

                        # Boucle aide
                        while clue:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                                    menu = False
                                    rules = False
                                    how_to = False
                                    form = False
                                    play = False
                                    warning = False
                                    clue = False
                                    remove = False
                                    run = False
                                if event.type == KEYDOWN:
                                    if event.key == K_q:
                                        pygame.display.update()
                                        clue = False
                        key = None

                    # Remise à zéro
                    elif key == 'R':
                        for i in range(size):
                            for j in range(size):
                                s = sudoku.getGrid().getSquare(i, j)
                                if not s.isFixed():
                                    sudoku.clearSquare(s)
                        key = None

                    # Si le niveau est le niveau 3, on vérifie que l'utilisateur gagne ou perd
                    if level == 3:
                        end = winOrLoose(error_counter, 3, sudoku.getGrid())

                    # Sinon, on vérifie que le sudoku est complet et correct
                    else:
                        end = sudoku.getGrid().complete_checked()

                    # Si le jeu continue (ni gagné, ni perdu)
                    if not end:

                        # Si une case est sélectionnée et qu'une action est demandée
                        if sudoku.getGrid().getSelected() and key != None:
                            coord = sudoku.getGrid().getSelected()
                            selected_square = sudoku.getGrid().getSquare(coord.getX(), coord.getY())

                            # Si la case n'est pas fixe
                            if not selected_square.isFixed():

                                # Effacer la case
                                if key == "E":
                                    sudoku.clearSquare(selected_square)

                                # Effacer tous les brouillons de la case
                                elif key == "D":
                                    sudoku.clearTrials(selected_square)

                                # Effacer un brouillon particulier de la case
                                elif key == "B":

                                    # Boucle effacement
                                    while remove:
                                        for event in pygame.event.get():
                                            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                                                menu = False
                                                rules = False
                                                how_to = False
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

                                else:
                                    # Si l'ajout est un brouillon
                                    if sudoku.getGrid().isSketching():
                                        if selected_square.getValue() == 0:
                                            sudoku.addTrial(selected_square, key)
                                        sudoku.getGrid().setSketching(False)

                                    else:
                                        sudoku.addValue(selected_square, key)
                                        sudoku.clearTrials(selected_square)

                                        # Si la grille est de niveau 1, alors la gestion des brouillons (effacement) est automatique
                                        if level == 1:
                                            for i in range(size):
                                                sudoku.removeTrial(sudoku.getGrid().getSquare(selected_square.getCoordinates().getX(), i), key) # Suppression de tous les brouillons de même ligne correspondant à la valeur entrée
                                                sudoku.removeTrial(sudoku.getGrid().getSquare(i, selected_square.getCoordinates().getY()), key) # Suppression de tous les brouillons de même colonne correspondant à la valeur entrée

                                            for p in sudoku.getGrid().getPiece(selected_square):
                                                # Suppression de tous les brouillons de même "super-carré" correspondant à la valeur entrée, si et seulement s'il existe
                                                if sudoku.getGrid().getSquare(p.getX(), p.getY()).haveTrial(key):
                                                    sudoku.removeTrial(sudoku.getGrid().getSquare(p.getX(), p.getY()), key)

                                        # Si la valeur renseignée correspond à celle entrée dans les solutions, alors l'attribut checked passe à True (pour signifier que la valeur est correcte)
                                        if grid_soluce[level - 1][selected_square.getCoordinates().getX() * size + selected_square.getCoordinates().getY()] == key:
                                            selected_square.setChecked(True)
                                        # Sinon la case est considérée comme incorrecte (cas où la valeur est modifiée même remplaçant une valeur correcte)
                                        else:
                                            selected_square.setChecked(False)

                                            # Si le niveau est le niveau 3, alors chaque valeur incorrecte est comptabilisée
                                            if level == 3:
                                                error_counter += 1

                        redrawWindow(fenetre, sudoku.getGrid(), level, False, white_color, light_blue_color, grey_color, average_blue_color, dark_color, grey_color, green_color, red_color)
                        pygame.display.update()
                        key = None

                    else:
                        # Création de l'arrière-plan
                        end_bg = pygame.Surface(fenetre.get_size())
                        end_bg = end_bg.convert()
                        end_bg.fill((255, 255, 255))

                        # Affichage du message de réussite
                        if sudoku.getGrid().complete_checked():
                            text = fnt_h2.render("Bravo !", 1, dark_blue_color)
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 150
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("Vous avez terminé", 1, dark_blue_color)
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 200
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("la grille avec succès !", 1, dark_blue_color)
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 250
                            end_bg.blit(text, textpos)

                        # Affichage du message d'échec
                        else:
                            text = fnt_h2.render("Oh... Quelle tristesse !", 1, dark_blue_color)
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 150
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("Vous avez perdu.", 1, dark_blue_color)
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 200
                            end_bg.blit(text, textpos)
                            text = fnt_h2.render("Retentez votre chance.", 1, dark_blue_color)
                            textpos = text.get_rect()
                            textpos.centerx = fenetre.get_rect().centerx
                            textpos.y = 250
                            end_bg.blit(text, textpos)

                        # Affichage du message de retour au menu
                        text = fnt_p.render("Appuyer sur la touche 'Entrée' pour revenir au menu.", 1, dark_color)
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
