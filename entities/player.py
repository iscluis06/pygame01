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
    MOVE_RIGHT = 1
    MOVE_LEFT = -1
    NO_MOVEMENT = 0


    def __init__(self, pos_x, pos_y):
        Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.time = None
        self.is_sound_played = False
        self.increment_x = 6
        self.current_movement = Player.NO_MOVEMENT

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.time and time.time() - self.time >= 2 and self.is_sound_played:
            print("removing")
            self.remove(self.containers)
        else:
            if self.current_movement != Player.NO_MOVEMENT:
                self.rect.x += self.increment_x * self.current_movement
            if "screen" in kwargs and self.rect.x > kwargs["screen"].get_width():
                print(f"screen: {kwargs['screen'].get_width()}\n current x: {self.rect.x}")
                self.rect.x = kwargs["screen"].get_width() - self.image.get_width()
                self.current_movement = Player.NO_MOVEMENT
            elif self.rect.x < 0:
                self.rect.x = 0
                self.current_movement = Player.NO_MOVEMENT


    def play_flush(self):
        if self.sound and not self.is_sound_played:
            self.sound.play()
            self.is_sound_played = True
            self.time = time.time()


    def player_movement(self, event: int, key: int):
        if event == pygame.KEYDOWN:
            if key == pygame.K_RIGHT:
                self.current_movement = self.MOVE_RIGHT
            elif key == pygame.K_LEFT:
                self.current_movement = self.MOVE_LEFT
            elif key == pygame.K_SPACE:
                Paper(self.rect.x, self.rect.y)
        if event == pygame.KEYUP:
            print("KEY UP")
            if key == pygame.K_LEFT or key == pygame.K_RIGHT:
                self.current_movement = Player.NO_MOVEMENT
