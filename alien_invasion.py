# Projetoo com pygame -> INVASÃO ALIEN

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():  # Função principal do game
    pygame.init()  # inicializa nosso projeto
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # variável que armazena as config da tela
    pygame.display.set_caption('INVASÃO ALIEN')  # Título que nossa tela terá
    ship = Ship(screen)
    while True:  # laço principal do jogo
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
