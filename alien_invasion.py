import sys
import pygame

def run_game():
    pygame.init();
    bg_color = (230,230,230);
    screem = pygame.display.set_mode((1024,740));
    pygame.display.set_caption("Alien invasion");
    while True:
        #Eventos do teclado.
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        #Tela recente fica visivel
        screem.fill(bg_color)
        pygame.display.flip()

run_game()