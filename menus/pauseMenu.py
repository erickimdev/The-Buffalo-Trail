import pygame
from text import *
from button import *

class PauseMenu:
    def __init__(self, game):
        self.game = game
        y_offset = 130

        # instantiate Game Paused header
        self.game_paused = Text('Game Paused', self.game.width/2, y_offset, 60, WHITE)

        # instantiate RESUME button
        self.resume_button = Button(539, y_offset+80, 200, 70, LIGHT_GRAY, False, self.game)
        self.resume_button_text = Text('Resume', self.game.width/2, y_offset+115, 30, BLACK)
        # instantiate SAVE button
        self.save_button = Button(539, y_offset+180, 200, 70, LIGHT_GRAY, False, self.game)
        self.save_button_text = Text('Save', self.game.width/2, y_offset+217, 30, BLACK)
        # instantiate OPTIONS button
        self.options_button = Button(539, y_offset+280, 200, 70, LIGHT_GRAY, False, self.game)
        self.options_button_text = Text('Options', self.game.width/2, y_offset+320, 30, BLACK)
        # instantiate QUIT button
        self.quit_button = Button(539, y_offset+380, 200, 70, LIGHT_GRAY, False, self.game)
        self.quit_button_text = Text('Quit', self.game.width/2, y_offset+420, 30, BLACK)

    def draw_screen(self):
        # draw Game Paused header
        self.game_paused.draw(self.game.screen)

        # draw buttons
        # RESUME button
        self.resume_button.draw(self.game.screen)
        self.resume_button_text.draw(self.game.screen)
        # SAVE button
        self.save_button.draw(self.game.screen)
        self.save_button_text.draw(self.game.screen)
        # OPTIONS button
        self.options_button.draw(self.game.screen)
        self.options_button_text.draw(self.game.screen)
        # QUIT button
        self.quit_button.draw(self.game.screen)
        self.quit_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch RESUME button click
        self.resume_button.change_menu(event, mx, my, "play")
        # catch OPTIONS button click
        self.options_button.change_menu(event, mx, my, "options")
        # catch QUIT button click
        self.quit_button.quit(event, mx, my)
        # catch SAVE button click
        self.save_button.change_menu(event, mx, my, "save_confirm")

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"