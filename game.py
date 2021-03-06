import pygame
from obj import Obj, Pipe, Coin, Bird
import random


class Game():

    def __init__(self):

        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.pipes_group = pygame.sprite.Group()
        
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        self.bird = Bird("assets/bird0.png", 50, 320, self.all_sprites)

        self.ticks = 0

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.move_bg()
        self.move_ground()
        self.spaw_pipes()
        self.bird.collision_pipes(self.pipes_group)
        self.bird.collision_coin(self.coin_group)
        self.all_sprites.update()

    def move_bg(self):
        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1

        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 0
        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 360
    
    def move_ground(self):
        self.ground.rect[0] -= 2
        self.ground2.rect[0] -= 2

        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 360

    def spaw_pipes(self):
        self.ticks += 1

        
        if self.ticks >= random.randrange(100, 200):
            self.ticks = 0
            pipe = Pipe("assets/pipe1.png", 360,random.randrange(280, 440), self.all_sprites, self.pipes_group)
            pipe2 = Pipe("assets/pipe2.png", 360, pipe.rect[1] - 550, self.all_sprites, self.pipes_group)
            coin = Coin("assets/0.png", 388, pipe.rect[1] - 100, self.all_sprites, self.coin_group)