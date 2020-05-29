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
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        print('Centerx: ', self.rect.centerx)
        self.rect.centerx = self.center