import pygame
import math
from pygame.locals import *
from button import *
from text import *


class Play:
    def __init__(self, game):
        self.game = game
        # MINOREVENT = 3
        # instantiate random text
        self.random_text = Text('GAME UNDER CONSTRUCTION', self.game.width / 2, 300, 50, WHITE)
        self.time = Text(str(math.floor(pygame.time.get_ticks() / 1000)), 1200, 50, 20, WHITE)
        self.inPlay = False
        # instantiate PAUSE GAME button
        self.pause_button = Button(10, 10, 35, 35, (210, 210, 210), False, self.game)
        self.pause_button_text = Text('II', 29, 29, 27, BLACK)

        # "major stop"
        self.major_stops_button = Button(100, 10, 60, 60, WHITE, False, self.game)
        self.major_stops_text = Text("Major", 120, 20, 20, BLACK)

    def draw_screen(self):
        # draw random
        self.random_text.draw(self.game.screen)
        # draw PAUSE button
        self.pause_button.draw(self.game.screen)
        self.pause_button_text.draw(self.game.screen)

        # draw timer
        self.time.text = str(math.floor(pygame.time.get_ticks() / 1000))
        self.time.draw(self.game.screen)

        # draw major stop filler
        self.major_stops_button.draw(self.game.screen)
        self.major_stops_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch PLAY button clicks
        self.pause_button.change_menu(event, mx, my, "pause")

        self.major_stops_button.change_menu(event, mx, my, "major")
        # press esc key to PAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "pause"
