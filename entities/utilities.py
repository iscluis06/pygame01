import time
from typing import Any

from pygame.sprite import Sprite


class Explosion(Sprite):
    containers = []
    images = []

    def __init__(self, pos_x, pos_y):
        Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.life_cycle = time.time()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if time.time() - self.life_cycle > 0.4:
            self.remove(self.containers)
