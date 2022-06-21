import pygame
from game import Game

class Main():

    def __init__(self):
        
        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("FlappyBird")

        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = Game()

    def events(self):

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def update(self):
        while self.loop:
             self.fps.tick(30)
             self.events()
             self.draw()
             pygame.display.update()

Main().update()




