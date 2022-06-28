import pygame


class Obj(pygame.sprite.Sprite):

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

class Pipe(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

    def update(self, *args):
        self.move()
    
    def move(self):
        self.rect[0] -= 2

        if self.rect[0] <= -100:
            self.kill()

class Coin(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect[0] -= 2

        if self.rect[0] <= -100:
            self.kill()

    def anim(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load("assets/" + str(self.ticks) + ".png")
         

class Bird(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.ticks = 0
        self.vel = 4
        self.grav = 1

    
    def update(self, *args):
        self.move()
        self.anim()

    def anim(self):
        self.ticks = (self.ticks + 1) % 4
        self.image = pygame.image.load("assets/bird" + str(self.ticks) + ".png")

    def move(self):
        key = pygame.key.get_pressed()

        self.vel += self.grav
        self.rect[1] += self.vel

        if self.vel >= 15:
            self.vel = 15
        


        if key[pygame.K_SPACE]:
            self.vel -= 3

        if self.rect[1] >= 440:
            self.rect[1] = 440
        elif self.rect[1] <= -10:
            self.rect[1] = -10
            self.vel = 4

    def collision_pipes(self, group):

        col = pygame.sprite.spritecollide(self, group, False)

        if col:
            self.play = False

    def collision_coin(self, group):

        col = pygame.sprite.spritecollide(self, group, True)

        if col:
            print("Coin")
