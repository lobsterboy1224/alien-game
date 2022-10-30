import pygame
from pygame.sprite import Sprite

"""This class inherits from Sprite. 
This allows us to group many Alien Ships together into a group, 
and then act on that group all at once"""
class Alien(Sprite):
    
    def __init__(self, sa_game,x,y):

        super().__init__()
        self.screen = sa_game.screen
        self.screen_rect = sa_game.screen.get_rect()

        # load the alien ship image
        self.image = pygame.image.load("alien.png")

        # set the image to an appropriate size
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.color = (100,100,100)

        self.moveRight = True

    #displays alien ship
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

    #moves ships left and right
    def update(self):
        if self.moveRight == True and self.rect.right == 1920:
            self.rect.y += 100
            self.rect.x -= 1
            self.moveRight = False
        elif self.moveRight == False and self.rect.left == 0:
            self.rect.y += 100
            self.rect.x += 1
            self.moveRight = True
        elif self.moveRight == True:
            self.rect.x += 1
        elif self.moveRight == False:
            self.rect.x -= 1
