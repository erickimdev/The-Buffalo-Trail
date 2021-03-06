import pygame
from pygame.locals import *
from button import *
from text import *
import random

class TalkToStranger:
    def __init__(self, game):
        self.game = game
        
        # instantiate select a person text 
        self.select_person_text = Text('Select a person to talk to', 750, 130, 25, WHITE)
        # instantiate text for stranger1
        self.stranger1_text = Text('A traveler like you', 700, 230, 25, WHITE)
        # instantiate text for stranger2
        self.stranger2_text = Text('2 townsmen walking towards you', 820, 330, 25, WHITE)
        # instantiate text for stranger3
        self.stranger3_text = Text('A random store clerk', 720, 430, 25, WHITE)

        x = 300
        y = 205
        # instantiate STRANGER1 button
        self.stranger1_button = Button(x, y, 200, 50, LIGHT_GRAY, False, self.game)
        self.stranger1_button_text = Text('Stranger 1', x+99, y+26, 22, BLACK)
        # instantiate STRANGER2 button
        self.stranger2_button = Button(x, y+100, 200, 50, LIGHT_GRAY, False, self.game)
        self.stranger2_button_text = Text('Stranger 2', x+99, y+126, 22, BLACK)
        # instantiate STRANGER3 button
        self.stranger3_button = Button(x, y+200, 200, 50, LIGHT_GRAY, False, self.game)
        self.stranger3_button_text = Text('Stranger 3', x+99, y+226, 22, BLACK)

        # instantiate BACK button
        self.back_button = Button(540, 520, 200, 70, LIGHT_GRAY, False, self.game)
        self.back_button_text = Text('Back', 640, 560, 30, BLACK)

    def draw_screen(self):
        #select a stranger
        self.select_person_text.draw(self.game.screen)
         #select stranger1
        self.stranger1_text.draw(self.game.screen)
         #select stranger2
        self.stranger2_text.draw(self.game.screen)
         #select stranger3
        self.stranger3_text.draw(self.game.screen)

        # Stranger1 button
        self.stranger1_button.draw(self.game.screen)
        self.stranger1_button_text.draw(self.game.screen)
        # Stranger2 button
        self.stranger2_button.draw(self.game.screen)
        self.stranger2_button_text.draw(self.game.screen)
        # Stranger3 button
        self.stranger3_button.draw(self.game.screen)
        self.stranger3_button_text.draw(self.game.screen)
        # Back button
        self.back_button.draw(self.game.screen)
        self.back_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        
        # catch stranger1 button click
        self.stranger1_button.change_menu(event, mx, my, "stranger1")  
        # catch stranger2 button click
        self.stranger2_button.change_menu(event, mx, my, "stranger2") 
        # catch stranger3 button click
        self.stranger3_button.change_menu(event, mx, my, "stranger3")  

        # catch back button click
        self.back_button.change_menu(event, mx, my, "pitstop")