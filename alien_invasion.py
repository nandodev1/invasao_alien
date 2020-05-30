import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import  Group


def run_game():
    pygame.init();
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.scren_height));

    #Cria espaçonave
    ship = Ship(ai_settings, screen)
    #Grupo de misséis
    bullets = Group()

    pygame.display.set_caption("Alien invasion");
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        gf.update_screen(ai_settings,screen,ship, bullets)
        #Tela recente fica visivel
        pygame.display.flip()

run_game()