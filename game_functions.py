import sys
import pygame
from bullet import Bullet


def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """Responde a teclas precionadas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Cria missél e coloca no grupo
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # solicitação de tecla solta
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza imagen na tela"""
    screen.fill(ai_settings.bg_color)
    #desenha misséis atráz da nave
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
