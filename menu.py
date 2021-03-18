import pygame
from pygame.locals import *
from button import *
from text import *
from colors import *
import shelve
#from game import *

#SAVE_DATA = shelve.open('Save Data')

pygame.init()
font = pygame.font.SysFont("comicsansms", 30)
class MainMenu:
    def __init__(self, game):
        self.game = game


        # instantiate game title header
        self.y_offset = 135
        self.the_buffalo = Text('THE BUFFALO', self.game.width / 2, self.y_offset, 75, WHITE)
        self.trail = Text('TRAIL', self.game.width / 2, self.y_offset + 95, 75, WHITE)

        # instantiate PLAY GAME button
        self.play_button = Button(200, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.play_button_text = Text('PLAY GAME', 340, 628, 28, BLACK)

        # instantiate OPTIONS button
        self.options_button = Button(800, 575, 250, 100, LIGHT_GRAY, False, self.game)
        self.options_button_text = Text('OPTIONS', 928, 628, 28, BLACK)

         # instantiate LOAD button
        self.load_button = Button(510, 575, 260, 100, LIGHT_GRAY, False, self.game)
        self.load_button_text = Text('LOAD', 640, 628, 28, BLACK)

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
        self.play_button.change_menu(event, mx, my, "username")

        # catch OPTIONS button clicks
        self.options_button.change_menu(event, mx, my, "options")

        # catch LOAD button clicks
        self.load_button.change_menu(event, mx, my, "load")
        
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
        # catch SAVE button click
        self.save_button.change_menu(event, mx, my, "save conformation")

        #DO SAVE FUNCTIONALITY HERES
        

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"

    
class LoadMenu:
    def __init__(self, game):
        self.game = game

        self.Load_text = Text('1 file found. Click NEXT to load the file', 700, 200, 50, WHITE)

        # instantiate BACK TO MAIN MENU button
        self.back_button = Button(510, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.back_button_text = Text('BACK', 640, 628, 28, BLACK)

        self.next_button = Button(910, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.next_button_text = Text('NEXT', 940, 628, 28, BLACK)
        shelfFile =shelve.open('saved data')
        self.game.difficulty = shelfFile('difficulty')
        shelfFile.close()

       # shelfFile = shelve.open('saved data')        

    def draw_screen(self):
        self.Load_text.draw(self.game.screen)

         # BACK button
        self.back_button.draw(self.game.screen)
        self.back_button_text.draw(self.game.screen)

        self.next_button.draw(self.game.screen)
        self.next_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch BACK button clicks
        self.back_button.change_menu(event, mx, my, "main")
        self.next_button.change_menu(event, mx, my, "play")



class SaveMenuConformation:
    def __init__(self, game):
        self.game = game

        self.conformation_text = Text('Do you want to save the game?', 700, 200, 50, WHITE)

        # instantiate YES button
        self.yes_button = Button(810, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.yes_button_text = Text('YES', 950, 628, 28, BLACK)

        # instantiate NO button
        self.no_button = Button(510, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.no_button_text = Text('NO', 640, 628, 28, BLACK)

    def draw_screen(self):
        self.conformation_text.draw(self.game.screen)

         # YES button
        self.yes_button.draw(self.game.screen)
        self.yes_button_text.draw(self.game.screen)

         # NO button 
        self.no_button.draw(self.game.screen)
        self.no_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        # catch No button clicks
        self.no_button.change_menu(event, mx, my, "pause")
        # catch Yes button clicks
        self.yes_button.change_menu(event, mx, my, "save")

class SaveMenu:
    def __init__(self, game):
        self.game = game

        self.save_text = Text('Under Construction.......', 700, 200, 50, WHITE)
        
        self.Back1_button = Button(510, 575, 275, 100, LIGHT_GRAY, False, self.game)
        self.Back1_button_text = Text('BACK', 640, 628, 28, BLACK)

    def draw_screen(self):
        self.save_text.draw(self.game.screen)
        
         # BACK button
        self.Back1_button.draw(self.game.screen)
        self.Back1_button_text.draw(self.game.screen)


    def catch_actions(self, event, mx, my):
        self.Back1_button.change_menu(event, mx, my, "play")
        

