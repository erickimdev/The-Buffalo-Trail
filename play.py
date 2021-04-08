import pygame
from pygame.locals import *
from button import *
from text import *
from menu import *

class Play:
    def __init__(self, game):
        self.game = game

        # instantiate random text
        self.random_text = Text('GAME UNDER CONSTRUCTION', self.game.width/2, 300, 50, WHITE)

        # instantiate PAUSE GAME button
        self.pause_button = Button(10, 10, 35, 35, (210,210,210), False, self.game)
        self.pause_button_text = Text('II', 29, 29, 27, BLACK)

         # instantiate Talk_to_stranger button
        self.Pit_stop_button = Button(1100, 10, 160, 30, LIGHT_GRAY, False, self.game)
        self.Pit_stop_button_text = Text('Pit Stop', 1180, 27, 13, BLACK)

    def draw_screen(self):
        # draw random
        self.random_text.draw(self.game.screen)

        # draw PAUSE button
        self.pause_button.draw(self.game.screen)
        self.pause_button_text.draw(self.game.screen)

        # draw Talk_to_stranger button
        self.Pit_stop_button.draw(self.game.screen)
        self.Pit_stop_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch PLAY button clicks
        self.pause_button.change_menu(event, mx, my, "pause")

        self.Pit_stop_button.change_menu(event, mx, my, "pitStop")

        # press esc key to PAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "pause"