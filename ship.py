import pygame

class Ship:
    def __init__(self,ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen
        #Load imagem
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Flags de movimentação
        self.moving_rigth = False
        self.moving_left = False

        #Inicia espaçonave no centro da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)



    def blitme(self):
        #desenha nave posição atual
        self.screen.blit(self.image,self.rect)

    def update(self):
        #atualiza a espaço de acordo com flag
        if self.moving_rigth:
            """Atualiza centro da espaço nave e não o retangulo"""
            if self.moving_rigth and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center