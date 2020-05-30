import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Classe para adiministrar os misséis"""

    def __init__(self, ai_settings, screen, ship):
        # cria missél na posição da nave
        super().__init__()
        self.screen = screen

        # Retangulo do projetil
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena posição do missel como um valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        # missél vai para cima
        self.y -= self.speed_factor
        # Atualiza a posição do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o missél na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
