from pygame.sprite import Sprite


class PooEnemy(Sprite):
    images = []
    containers = []

    def __init__(self, pos_x, pos_y, level):
        Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.enemyRight = True
        self.accel = 5 * level

    def update(self, **kwargs):
        if (kwargs['screen']
                and self.rect.x >= 0
                and self.rect.x + self.image.get_width() <= kwargs['screen'].get_width()):
            if (self.enemyRight
                    and self.rect.x + self.image.get_width() + self.accel <= kwargs['screen'].get_width()):
                self.rect.x += self.accel
            elif (self.enemyRight == False and self.rect.x - self. accel >= 0):
                self.rect.x -= self.accel
            if (self.rect.x == 0
                    or self.rect.x - self.accel < 0
                    or self.rect.x + self.image.get_width() == kwargs['screen'].get_width()
                    or self.rect.x + self.image.get_width() + self.accel > kwargs['screen'].get_width()):
                self.enemyRight = not self.enemyRight
                self.rect.y += 40