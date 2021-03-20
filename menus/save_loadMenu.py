import pygame
from text import *
from button import *
import os

class LoadMenu:
    def __init__(self, game):
        self.game = game

        self.load_text_found = Text('GAME LOADED', self.game.width / 2, 250, 65, WHITE)
        self.load_text_notfound = Text('No Save Data Found', self.game.width / 2, 250, 65, WHITE)

        # instantiate BACK TO MAIN MENU button
        self.back_button = Button(550, 575, 220, 85, LIGHT_GRAY, False, self.game)
        self.back_button_text = Text('BACK', 660, 622, 28, BLACK)

        self.next_button = Button(550, 575, 220, 85, LIGHT_GRAY, False, self.game)
        self.next_button_text = Text('NEXT', 660, 622, 28, BLACK)

    def draw_screen(self):
        # txt file NOT empty
        if os.stat("save.txt").st_size != 0:
            # draw "GAME LOADED"
            self.load_text_found.draw(self.game.screen)

            # draw NEXT button
            self.next_button.draw(self.game.screen)
            self.next_button_text.draw(self.game.screen)

        # txt file is empty (no game saved)
        else:
            # draw "No Save Data Found"
            self.load_text_notfound.draw(self.game.screen)

            # draw BACK button
            self.back_button.draw(self.game.screen)
            self.back_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # txt file NOT empty
        if os.stat("save.txt").st_size != 0:
            # catch NEXT button clicks
            self.next_button.change_menu(event, mx, my, "play")
        else:
            # catch BACK button clicks
            self.back_button.change_menu(event, mx, my, "main")

class SaveMenu:
    def __init__(self, game):
        self.game = game

        self.save_text = Text("GAME SAVED", self.game.width/2, 200, 65, WHITE)
        self.Back1_button = Button(530, 575, 270, 100, LIGHT_GRAY, False, self.game)
        self.Back1_button_text = Text('BACK', 670, 628, 28, BLACK)

    def draw_screen(self):
        self.save_text.draw(self.game.screen)
        self.Back1_button.draw(self.game.screen)
        self.Back1_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        self.Back1_button.change_menu(event, mx, my, "play")

class SaveMenuConfirmation:
    def __init__(self, game):
        self.game = game

        self.confirmation_text = Text('Save Game?', self.game.width/2, 230, 65, WHITE)

        # instantiate NO button
        self.no_button = Button(378, 575, 220, 85, LIGHT_GRAY, False, self.game)
        self.no_button_text = Text('NO', 488, 622, 28, BLACK)

        # instantiate YES button
        self.yes_button = Button(675, 575, 220, 85, LIGHT_GRAY, False, self.game)
        self.yes_button_text = Text('YES', 785, 622, 28, BLACK)

    def draw_screen(self):
        self.confirmation_text.draw(self.game.screen)

        # YES button
        self.yes_button.draw(self.game.screen)
        self.yes_button_text.draw(self.game.screen)

        # NO button
        self.no_button.draw(self.game.screen)
        self.no_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch NO button clicks
        self.no_button.change_menu(event, mx, my, "pause")
        # catch YES button clicks
        self.yes_button.change_menu(event, mx, my, "save")