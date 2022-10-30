import pygame
from pygame.sprite import Sprite


"""This class inherits from Sprite. 
This allows us to group many LaserBlasts together into a group, 
and then act on that group all at once"""
class LaserBlast(Sprite):

    speed = 1.0

    def __init__(self,sa_game):

        super().__init__()

        self.screen = sa_game.screen
        self.color = (60,60,60)

        #our laser blasts aren't going to be based on an image
        #so we build a rect object for them
        self.rect = pygame.Rect(0,0,3,15)

        #set the laser blast to be initally located at the top of the ship
        self.rect.midtop = sa_game.spaceship.rect.midtop

        self.y = float(self.rect.y)

    #moves laser blasts
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    #draws laser blasts
    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

