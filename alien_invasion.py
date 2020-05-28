import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init();
    ai_settings = Settings()
    screem = pygame.display.set_mode((ai_settings.screen_width,ai_settings.scren_height));

    #Cria espaçonave
    ship = Ship(screem)

    pygame.display.set_caption("Alien invasion");
    while True:
        gf.check_events()
        #Tela recente fica visivel
        screem.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()