import pygame
from text import *
from button import *

class EndingMenu:
    def __init__(self, game):
        self.game = game
        y_offset = 130

        # instantiate Game Paused header
        self.congrats1_text = Text('Congratulations!', self.game.width/2, y_offset, 60, WHITE)
        self.congrats2_text = Text('You have reached Buffalo', self.game.width/2, y_offset + 100, 30, WHITE)

        # instantiate PLAY AGAIN button
        self.playAgain_button = Button(539, y_offset+400, 200, 70, LIGHT_GRAY, False, self.game)
        self.playAgain_button_text = Text('Play Again', self.game.width/2, y_offset+435, 25, BLACK)

        # instantiate bison image
        self.bison = pygame.image.load('assets/bison.png')
        self.bison = pygame.transform.scale(self.bison, (399, 269))

    def draw_screen(self):
        # draw Congratulations header
        self.congrats1_text.draw(self.game.screen)
        self.congrats2_text.draw(self.game.screen)

        # draw PLAY AGAIN button
        self.playAgain_button.draw(self.game.screen)
        self.playAgain_button_text.draw(self.game.screen)

        # draw BISON png
        self.game.screen.blit(self.bison, (300, 300))
        self.game.screen.blit(self.bison, (550, 300))

    def catch_actions(self, event, mx, my):
        # catch PLAY AGAIN button click
        self.playAgain_button.change_menu(event, mx, my, "play")

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"