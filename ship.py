# Classe responsável por fazer a configuração da navve espacial

import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('imagens/rocket-312767_1280.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # iniciando a espaço nave na parte central e inferior da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # desennhado na tela
    def blitme(self):
        self.screen.blit(self.image, self.rect)
