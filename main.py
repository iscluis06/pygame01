import os
from typing import List

import pygame
from pygame.sprite import Group
from guppy import hpy
from pygame.surface import Surface

from entities.enemies import PooEnemy
from entities.missiles import Paper
from entities.player import Player
from entities.utilities import Explosion


def start_game(name):
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    player_group, enemy_group, player_missiles, explosions_group = Group(), Group(), Group(), Group()

    # Sound loading
    fart = pygame.mixer.Sound("./fart.wav")
    splat = pygame.mixer.Sound("./splat.wav")

    # Cargando imagenes
    explosion = pygame.image.load("./explosion.png")
    background = pygame.image.load("./bathroom.jpg")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    poo = pygame.image.load("./poo.png").convert()
    paper = pygame.image.load("./toilet-paper.png").convert()
    Explosion.images = [explosion]
    PooEnemy.images = [poo]
    Player.images = [pygame.image.load("./toilet-paper-stack.png").convert(paper)]
    Paper.images = [pygame.transform.scale(paper,(38, 38))]

    Paper.sound = fart
    Player.sound = splat

    Explosion.containers = explosions_group
    Player.containers = player_group
    Paper.containers = player_missiles
    PooEnemy.containers = enemy_group

    pygame.display.set_caption("Flying shit")
    player = Player(370, 480)

    pygame.display.set_icon(poo)

    level = 1

    create_enemies(level)

    while player.alive():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type and hasattr(event, 'key'):
                player.player_movement(event.type, event.key)

        if not player.is_sound_played:
            screen.fill((0, 0, 0))

            enemy_group.update(screen=screen)
            player_missiles.update(screen=screen)

            screen.blit(background, (0, 0))
            enemy_group.draw(screen)
            player_group.update(screen=screen)
            player_group.draw(screen)
            player_missiles.draw(screen)
            collision = pygame.sprite.groupcollide(enemy_group, player_missiles, True, True)
            if collision:
                for key in dict.keys(collision):
                    sprite: Paper = collision[key][0]
                    sprite.play_plop()
                    Explosion(sprite.rect.x, sprite.rect.y)
            player_collision = pygame.sprite.spritecollide(player, enemy_group, False)
            if player_collision:
                player.play_flush()
            explosions_group.draw(screen)
            explosions_group.update()
            pygame.display.update()
            if len(enemy_group) == 0:
                level += 1
                create_enemies(level)
            clock.tick(60)
        else:
            player.update()


def create_enemies(level):
    current_width = PooEnemy.images[0].get_width()
    current_height = PooEnemy.images[0].get_height()
    for y in range(5):
        for x in range(9):
            pos_y = 1 if y == 0 \
                else (current_height * 2 * y)
            pos_x = 1 if x == 0 \
                else (current_width * 3 * x)
            PooEnemy(pos_x, pos_y, level)
            print(f"Posiciones X: {pos_x} Y: {pos_y}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game('PyCharm')
