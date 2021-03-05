# Classe responsável por fazer a configuração da navve espacial

import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('imagens/rocket-312767_1280.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    # Atualiza a posição da espaço nave através da flag self.moving_right
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1


    # desennhado na tela
    def blitme(self):
        self.screen.blit(self.image, self.rect)
