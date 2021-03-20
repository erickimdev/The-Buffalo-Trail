import pygame
from text import *
from button import *

class MainMenu:
    def __init__(self, game):
        self.game = game

        # instantiate game title header
        self.y_offset = 135
        self.the_buffalo = Text('THE BUFFALO', self.game.width / 2, self.y_offset, 75, WHITE)
        self.trail = Text('TRAIL', self.game.width / 2, self.y_offset + 95, 75, WHITE)

        x = 230
        # instantiate PLAY GAME button
        self.play_button = Button(x, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.play_button_text = Text('PLAY GAME', x+140, 628, 28, BLACK)

        # instantiate LOAD button
        self.load_button = Button(x+310, 575, 260, 100, LIGHT_GRAY, False, self.game)
        self.load_button_text = Text('LOAD GAME', x+440, 628, 28, BLACK)

        # instantiate OPTIONS button
        self.options_button = Button(x+600, 575, 250, 100, LIGHT_GRAY, False, self.game)
        self.options_button_text = Text('OPTIONS', x+728, 628, 28, BLACK)

    def draw_screen(self):
        # draw game name
        self.the_buffalo.draw(self.game.screen)
        self.trail.draw(self.game.screen)

        # draw buttons
        # PLAY GAME button
        self.play_button.draw(self.game.screen)
        self.play_button_text.draw(self.game.screen)
        # OPTIONS button
        self.options_button.draw(self.game.screen)
        self.options_button_text.draw(self.game.screen)
        # LOAD button
        self.load_button.draw(self.game.screen)
        self.load_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch PLAY button clicks
        self.play_button.change_menu(event, mx, my, "play")

        # catch OPTIONS button clicks
        self.options_button.change_menu(event, mx, my, "options")

        # catch LOAD button clicks
        self.load_button.change_menu(event, mx, my, "load")

        # press esc key to quit
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()