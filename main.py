import os
from typing import List

import pygame, psutil
from guppy import hpy
from pygame.surface import Surface


def print_hi(name):
    #current_heap = hpy()
    #current_heap.setrelheap()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Flying shit")
    poo = pygame.image.load("./poo.png").convert()
    stack = pygame.image.load("./toilet-paper-stack.png").convert()
    paper = pygame.image.load("./toilet-paper.png").convert()
    stackX = 370
    stackY = 480
    enemyX, enemyY = 0, 0
    enemyRight = True
    increaseX = 0
    projectile_array: list[Entity] = []
    pygame.display.set_icon(poo)

    running = True
    enemy_array: list[list[Enemy]] = [[Poo(0, 0) for y in range(1, 9)] for x in range(1, 5)]

    for y in range(len(enemy_array)):
        for enemy in enemy_array[y]:
            print(f"enemy index {enemy_array[y].index(enemy)}")
            enemy.posY = 1 if y == 0 + enemy.image.get_width() \
                else (enemy.image.get_height() * 2 * y)
            enemy.posX = 1 if enemy_array[y].index(enemy) == 0 + enemy.image.get_height() \
                else (enemy.image.get_width() * 3 * enemy_array[y].index(enemy))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    increaseX = 3
                    #print(stackX)
                if event.key == pygame.K_LEFT:
                    increaseX = -3
                    #print(stackX)
                if event.key == pygame.K_SPACE:
                     projectile_array.append(Paper(stackX, stackY-stack.get_height()))
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        increaseX = 0

        if(stackX >= 0
            and stackX + increaseX >= 0
            and stackX <= screen.get_width()-stack.get_width()
            and stackX + stack.get_width() + increaseX <= screen.get_width()):
            #print( f"stackX: {stackX + stack.get_width()} \n with_increase: {stackX+ stack.get_width() +increaseX}\n current screen width: {screen.get_width()}")
            stackX += increaseX





        screen.fill((0, 0, 0))

        for y in range(len(enemy_array)):
            for enemy in enemy_array[y]:
                
                enemy.movement(screen)
                screen.blit(enemy.image, (enemy.posX, enemy.posY))

        screen.blit(stack, (stackX, stackY))
        for projectile                   in projectile_array:
            screen.blit(projectile.image, (projectile.posX,       projectile.posY))
            projectile.posY -= 1
            if(projectile.posY < 0):
                projectile_array.remove(projectile)
        pygame.display.update()
        #print(f"current heap: {(current_heap.heap().size/1024)/1024}MB")
        #print(f"current RAM usage: {(psutil.Process(os.getpid()).memory_info().rss/1024)/1024}MB")


class Entity:
    def __init__(self, X: int, Y:int, image: Surface):
        self.posX = X
        self.posY = Y
        self.image = image


class Enemy(Entity):
    def __init__(self, X: int, Y:int, image: Surface, accel: int = 0.5):
        super().__init__(X, Y, image)
        self.accel = accel

    def attack(self, screen):
        pass

    def movement(self, screen):
        pass


class Poo(Enemy):
    def __init__(self, X: int, Y:int, accel: int = 0.2):
        super().__init__(X, Y, pygame.image.load("./poo.png").convert(), accel)
        self.enemyRight = True

    def movement(self, screen):
        if (self.posX >= 0
                and self.posX + self.image.get_width() <= screen.get_width()):
            if (self.enemyRight and self.posX + self.image.get_width() + self.accel <= screen.get_width()):
                self.posX += self.accel
            elif (self.enemyRight == False and self.posX - self.accel >= 0):
                self.posX -= self.accel
            if (self.posX == 0
                    or self.posX - self.accel < 0
                    or self.posX + self.image.get_width() == screen.get_width()
                    or self.posX + self.image.get_width() + self.accel > screen.get_width()):
                self.enemyRight = not self.enemyRight
                self.posY += 10
                # print(f"enemyY {enemyY}")


class Paper(Entity):
    def __init__(self, X: int, Y:int ):
        super().__init__(X, Y, pygame.image.load("./toilet-paper.png").convert())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

