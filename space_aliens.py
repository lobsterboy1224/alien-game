import sys, pygame
from ship import Ship
from alien import Alien
from LaserBlast import LaserBlast
'''
space_aliens.py

makes a game that allows you to move your ship left and right and press spacebar to shoot lasers at aliens. 
when all the aliens are dead, you win and the game is over.

programmer:blake leitch
date: 1/20/21
'''
class space_aliens:

    def __init__(self):
        pygame.init()
        pygame.font.init()

        #get a Surface object for the screen
        size = (1920,1020)
        self.screen = pygame.display.set_mode(size)
        self.screen_rect = self.screen.get_rect()

        #set the caption for the screen
        pygame.display.set_caption("Space Aliens: Space CS 328 Assignment 2 Blake Leitch")

        #set the background color
        self.bg_color = (20,0,0)

        #initiate spaceship, aliens, and blasts
        self.spaceship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.blasts = pygame.sprite.Group()

        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

        #counts how many times aliens have died
        self.counter = 0

        self.youLose = False
        self.youWin = False


        #creates alien swarm
        for self.i in range (13):
            myAlien = Alien(self,self.i*150,0)
            self.aliens.add(myAlien)

        #intizializes almost all sounds
        self.explosionSound = pygame.mixer.Sound('8-bit-explosion.wav')
        self.explosionSound.set_volume(0.3)
        self.deathSound = pygame.mixer.Sound('scream4.wav')
        self.winSound = pygame.mixer.Sound('child.wav')
        self.music = pygame.mixer.Sound('music.wav')
        self.music.set_volume(0.4)
        self.music.play()

    def fire_laser_blast(self):
        myBlast = LaserBlast(self)
        self.blasts.add(myBlast)
        sound = pygame.mixer.Sound('8-bit-laser.wav')
        sound.set_volume(0.1)
        sound.play()

    def start(self):

        while 1: #event loop

            #spin through all of the events looking for quit
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fire_laser_blast()
                if event.type == pygame.QUIT: 
                    sys.exit()

            #moves your spacship
            if event.type == pygame.KEYDOWN and self.youLose == False:
                if event.key == pygame.K_LEFT:
                    if self.spaceship.rect.left > 0:
                        self.spaceship.move(1)
                elif event.key == pygame.K_RIGHT:
                    if self.spaceship.rect.right < self.screen_rect.right:
                        self.spaceship.move(2)

            #check if blaster hits alien ships and if you killed them all or not
            if pygame.sprite.groupcollide(self.blasts, self.aliens, True, True):
                self.counter += 1
                print(self.counter)
                pygame.mixer.find_channel(True).queue(self.explosionSound)
                if self.i+1 == self.counter:
                    self.winSound.set_volume(0.4)
                    pygame.mixer.find_channel(True).queue(self.winSound)
                    self.youWin = True

            #erase the screen by filling it with the color specified earlier
            self.screen.fill(self.bg_color)

            #if spaceship collides with you
            if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
                self.deathSound.set_volume(0.1)
                pygame.mixer.find_channel(True).queue(self.deathSound)
                self.youLose = True

            #initializes all text
            self.font = pygame.font.Font('freesansbold.ttf', 100)
            self.textLose = self.font.render('you lose', True, self.green, self.blue)
            self.textLoseRect = self.textLose.get_rect()
            self.textLoseRect.center = (960, 500)
            self.textWin = self.font.render('you win! you killed ' + str(self.counter) + ' aliens!', True, self.green, self.blue)
            self.textWinRect = self.textWin.get_rect()
            self.textWinRect.center = (960, 500)

            #you lose!
            if self.youLose == True:
                self.music.stop()
                self.screen.blit(self.textLose, self.textLoseRect)
            #you win!
            if self.youWin == True:
                self.music.stop()
                self.screen.blit(self.textWin, self.textWinRect)

            self.blasts.update()
            self.aliens.update()
            for b in self.blasts.sprites():
                b.draw_laser()
            for a in self.aliens.sprites():
                a.draw_alien()
                
            #display the ship
            self.spaceship.blit()
            #updates the screen
            pygame.display.flip()


"""This section looks at a special python variable called __name__
This variablie is set when the program is executed.
If the value of __name__ is set to "__main__", 
then we know the file is being run as the main method for the program.
So, since we are the main program we'll create an instance of our class
and then call the start() method."""
if __name__ == '__main__':
    myGame = space_aliens()
    myGame.start()                

