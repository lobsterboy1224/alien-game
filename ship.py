import pygame

"""This class includes the ship, including
the ships appearane, how it moves, and its ability
to appear on screen."""
class Ship:

    def __init__(self,sa_game):

        self.screen = sa_game.screen
        self.screen_rect = sa_game.screen.get_rect()

        #load the space ship image
        self.image = pygame.image.load("ship.png")

		#set the image to an appropriate size
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

        #set the midbottom value of the ship to be the same as the 
        #midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    #displays ship
    def blit(self):
        self.screen.blit(self.image,self.rect)
    #moves ship
    def move(self, var):
        if var == 1:
            self.rect.x -= 1
        elif var == 2:
            self.rect.x += 1
        
