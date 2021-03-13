import pygame
from pygame.locals import *
from button import *
from text import *
from colors import *

class MainMenu:
    def __init__(self, game):
        self.game = game

        # instantiate game title header
        self.y_offset = 135
        self.the_buffalo = Text('THE BUFFALO', self.game.width / 2, self.y_offset, 75, WHITE)
        self.trail = Text('TRAIL', self.game.width / 2, self.y_offset + 95, 75, WHITE)

        # instantiate PLAY GAME button
        self.play_button = Button(300, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.play_button_text = Text('PLAY GAME', 440, 628, 28, BLACK)

        # instantiate OPTIONS button
        self.options_button = Button(800, 575, 250, 100, LIGHT_GRAY, False, self.game)
        self.options_button_text = Text('OPTIONS', 928, 628, 28, BLACK)

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

    def catch_actions(self, event, mx, my):
        # catch PLAY button clicks
        self.play_button.change_menu(event, mx, my, "play")

        # catch OPTIONS button clicks
        self.options_button.change_menu(event, mx, my, "options")

        # press esc key to quit
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()

class OptionsMenu:
    def __init__(self, game):
        self.game = game

        # instantiate OPTIONS header
        self.options_header = Text('OPTIONS', self.game.width/2, 90, 70, WHITE)

        x = 900
        y = 300
        # instantiate DIFFICULTY text
        self.difficultyText = Text('Difficulty', x+92, y-42, 40, WHITE)
        # instantiate EASY button
        self.easy_button = Button(x, y, 200, 60, LIGHT_GRAY, False, self.game)
        self.easy_button_text = Text('Easy', x+100, y+30, 30, BLACK)
        # instantiate MEDIUM button
        self.medium_button = Button(x, y+80, 200, 60, LIGHT_GRAY, False, self.game)
        self.medium_button_text = Text('Medium', x+100, y+110, 30, BLACK)
        # instantiate HARD button
        self.hard_button = Button(x, y+160, 200, 60, LIGHT_GRAY, False, self.game)
        self.hard_button_text = Text('Hard', x+100, y+190, 30, BLACK)

    def draw_screen(self):
        # draw OPTIONS header
        self.options_header.draw(self.game.screen)
        # draw DIFFICULTY text
        self.difficultyText.draw(self.game.screen)

        # shade current difficulty button
        if self.game.difficulty == "easy":
            self.easy_button.color = DARK_GRAY
        elif self.game.difficulty == "medium":
            self.medium_button.color = DARK_GRAY
        elif self.game.difficulty == "hard":
            self.hard_button.color = DARK_GRAY

        # draw buttons
            # EASY button
        self.easy_button.draw(self.game.screen)
        self.easy_button_text.draw(self.game.screen)
            # MEDIUM button
        self.medium_button.draw(self.game.screen)
        self.medium_button_text.draw(self.game.screen)
            # HARD button
        self.hard_button.draw(self.game.screen)
        self.hard_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # right click/ESC key goes to MainMenu OR PauseMenu
        if (event.type == MOUSEBUTTONDOWN and event.button == 3)\
                or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            # if Options clicked from main menu ONLY
            if not self.game.paused:
                self.game.menu_state = "main"
            elif self.game.paused:
                self.game.menu_state = "pause"

        # catch difficulty changes
        self.easy_button.change_difficulty(event, mx, my, "easy", self.medium_button, self.hard_button)
        self.medium_button.change_difficulty(event, mx, my, "medium", self.easy_button, self.hard_button)
        self.hard_button.change_difficulty(event, mx, my, "hard", self.easy_button, self.medium_button)

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

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"