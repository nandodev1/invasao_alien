import pygame

class Ship:
    def __init__(self,screen):
        self.screen = screen
        #Load imagem
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Inicia espaçonave no centro da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #desenha nave posição atual
        self.screen.blit(self.image,self.rect)