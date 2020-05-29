import sys
import pygame


def check_keydown_events(event, ship):
    """Responde a teclas precionadas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    # solicitação de tecla solta
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(event, ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Atualiza imagen na tela"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
