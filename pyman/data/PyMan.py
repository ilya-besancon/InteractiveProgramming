"""
@ilya-besancon
A simple game where a snake eats oranges!
"""

import os, sys
import pygame
import pygame.locals
from helpers import*
# from helpers import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


class PyManMain:
    """ The Main PyMan Class – This class handles the
    main initialization and creating of the Game"""

    def __init__(self, width=640, height=480):
        """ Initialize
        Initialize PyGame """
        pygame.init()
        # Set the window Size
        self.width = width
        self.height = height
        # Create the Screen
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        """ This is the Main Loop of the Game """
        """ Load All of our Sprites """
        self.LoadSprites()
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(100, 20)
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.snake.move(event.key)
                    if (event.key == K_q):
                        sys.exit()
                    if (event.key == K_r):
                        MainWindow.MainLoop()

            """Check for collision"""
            lstCols = pygame.sprite.spritecollide(self.snake
                                                 , self.pellet_sprites
                                                 , True)

            """Update the amount of pellets eaten"""
            self.snake.pellets = self.snake.pellets + len(lstCols)

            """Do the Drawging"""
            self.screen.blit(self.background, (0, 0))
            if pygame.font:
                font = pygame.font.Font(None, 45)
                text = font.render("Hearts: %s" %
                                   self.snake.pellets, 1, (32, 178, 170))
                textpos = text.get_rect(centerx=self.background.get_width()/2,
                                        centery=20)
                self.screen.blit(text, textpos)
                Vert = int(self.width/73)
                Horz = int(self.height/73)
                victory_y = 200
                offset = 50
                if self.snake.pellets == Vert * Horz:
                    font = pygame.font.Font(None, 100)
                    victory = font.render('You Won!', 1, (95, 168, 160))
                    textpos_vic = victory.get_rect(centerx=self.background.get_width()/2,
                                               centery=victory_y)
                    font_res = pygame.font.Font(None, 40)
                    restart = font_res.render('(Hit r to restart)', 1, (176, 226, 230))
                    textpos_res = restart.get_rect(centerx=self.background.get_width()/2,
                                               centery=victory_y + offset)
                    quit = font_res.render('(Hit q to quit)', 1, (176, 226, 230))
                    textpos_quit = quit.get_rect(centerx=self.background.get_width()/2,
                                               centery=victory_y + 2*offset)
                    self.screen.blit(victory, textpos_vic)
                    self.screen.blit(restart, textpos_res)
                    self.screen.blit(quit, textpos_quit)
                    # pygame.display.flip()
            self.pellet_sprites.draw(self.screen)
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        # Load the sprites that we need
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
        # figure out how many pellets we can display:
        nNumHorizontal = int(self.width/73)
        nNumVertical = int(self.height/73)
        # Create the Pellet group:
        self.pellet_sprites = pygame.sprite.Group()
        # Create all of the pellets and add them to the pellet_sprites group:
        for x in range(nNumHorizontal):
            for y in range(nNumVertical):
                self.pellet_sprites.add(Pellet(
                    pygame.Rect(x*(64 + 10) + 10, y*(64 +10) + 35, 64, 64)))


class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('snake.png', -1)
        self.pellets = 0
        self.x_dist = 10
        self.y_dist = 10

    def move(self, key):
        """ Move your self in one of the 4 directions according to key
        Key is the pyGame define for either up,down,left, or right key
        we will adjust ourselves in that direction """
        xMove = 0
        yMove = 0
        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        self.rect.move_ip(xMove, yMove)


class Pellet(pygame.sprite.Sprite):
    """ These are the pellets that the snake will eat! """

    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('heart.png', -1)
        if rect != None:
            self.rect = rect


if __name__ == "__main__":
    MainWindow = PyManMain(1000,1000)
    MainWindow.MainLoop()