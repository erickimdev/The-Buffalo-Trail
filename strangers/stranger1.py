import pygame
from pygame.locals import *
from button import *
from text import *
import random

class Stranger:
    def __init__(self, game):
        self.game = game
        
        # instantiate select a person text 
        self.person_text1 = Text('Traveler JACK:', 650, 130, 25, WHITE)
        self.person_text2 = Text('Better take some extra clothes. The cold is starting to kick in.', 650, 230, 25, WHITE)
        self.person_text3 = Text('Enjoy the journey while you can...', 620, 330, 25, WHITE)

        # instantiate BACK button
        self.back_button = Button(540, 520, 200, 70, LIGHT_GRAY, False, self.game)
        self.back_button_text = Text('Back', 640, 560, 30, BLACK)

    def draw_screen(self):
        # stranger's text
        self.person_text1.draw(self.game.screen)
        self.person_text2.draw(self.game.screen)
        self.person_text3.draw(self.game.screen)

        # BACK button
        self.back_button.draw(self.game.screen)
        self.back_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch BACK button click
        self.back_button.change_menu(event, mx, my, "stranger")