"""Script d'interface
Auteur : Charlotte Dujardin
Date : 28 décembre 2019"""

import pygame
from pygame.locals import *
import os
import traceback # récupération des informations sur les erreurs

import game
from game import *

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

    # Création de l'arrière-plan
    background = pygame.Surface(fenetre.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Affichage du menu
    font = pygame.font.Font(None, 36)
    text = font.render("Sudoku", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = fenetre.get_rect().centerx
    background.blit(text, textpos)

    def redraw_window(win, board, strikes):
        win.fill((255, 255, 255))
        fnt = pygame.font.SysFont("Arial", 20)
        text = fnt.render("X " * strikes, 1, (255, 0, 0))
        win.blit(text, (20, 560))
        board.drawGrid(win)

    # BOUCLE INFINIE
    key = None
    run = True
    strikes = 0

    grid = Grid(1, 9, 400, 400, grid_empty[0])
    sudoku = Sudoku(grid)

    while run:
        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    # Supprimer la valeur
                    key = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = sudoku.click(pos)
                if clicked:
                    sudoku.select(clicked)
                    key = None

            if sudoku.getGrid().getSelected() and key != None:
                coord = sudoku.getGrid().getSelected()
                sudoku.addValue(sudoku.getGrid().getSquare(coord.getX(), coord.getY()), key)

            redraw_window(fenetre, sudoku.getGrid(), strikes)
            pygame.display.update()

except:
    traceback.print_exc()

finally:
    pygame.quit()
    exit()