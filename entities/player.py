import time
from typing import Any

import pygame
from pygame.mixer import Sound
from pygame.sprite import Sprite

from entities.missiles import Paper


class Player(Sprite):
    images = []
    containers = []
    sound: Sound = None


    def __init__(self, pos_x, pos_y):
        Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.time = None
        self.is_sound_played = False
        self.increment_x = 2
        self.current_speed = 0
        self.top_speed = 4

    def update(self, *args: Any, **kwargs: Any) -> None:
        if time.time() - self.time >= 2 and self.is_sound_played:
            print("removing")
            self.remove(self.containers)
        else:
            self.rect.x += self.current_speed

    def play_flush(self):
        if self.sound and not self.is_sound_played:
            self.sound.play()
        elif self.is_sound_played:
            self.is_sound_played = True
            self.time = time.time()



    def player_movement(self, event: int, key: int):
        if event == pygame.KEYDOWN:
            if key == pygame.K_RIGHT and self.current_speed < self.top_speed:
                self.current_speed += self.increment_x
            elif key == pygame.K_LEFT and self.current_speed >0:
                self.current_speed -= self.increment_x
            elif key == pygame.K_SPACE:
                Paper(self.rect.x, self.rect.y)
        if event == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.current_speed = 0
