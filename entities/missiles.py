from typing import Any

from pygame.mixer import Sound
from pygame.sprite import Sprite


class Paper(Sprite):
    images = []
    containers = []
    sound: Sound = None

    def __init__(self, pos_x, pos_y):
        Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.y_speed = 12

    def update(self, *args: Any, **kwargs: Any) -> None:
        if kwargs["screen"]:
            if self.rect.y + self.image.get_height() > 0:
                self.rect.y -= self.y_speed
            else:
                self.remove(self.containers)

    def play_plop(self):
        if self.sound:
            self.sound.play()
