import pygame
from openpyxl import *
from random import *
from pygame.locals import *
from button import *
from menus.popUp import Popup
from text import *
from play import *
from menus import mainMenu
from menus import optionsMenu
from menus import pauseMenu
from menus import save_loadMenu

MINOREVENT = 3

class Game:
    def __init__(self):
        # initialize game
        pygame.init()
        self.minor = False
        # set width/height and display screen
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.popUp = Popup(self)
        self.prev_state = ""
        pygame.display.set_caption("The Buffalo Trail - Created by Pythoneers")
        # set difficulty - easy, medium, hard
        self.difficulty = "medium"

        # instantiate game's menu
        # "main"
        self.main_menu = mainMenu.MainMenu(self)
        # "options"
        self.options_menu = optionsMenu.OptionsMenu(self)
        # "play"
        self.gameplay = Play(self)
        # "pause"
        self.pause_menu = pauseMenu.PauseMenu(self)
        # "load"
        self.load_menu = save_loadMenu.LoadMenu(self)
        # "save_confirm"
        self.save_confirmation = save_loadMenu.SaveMenuConfirmation(self)
        # "save"
        self.save_menu = save_loadMenu.SaveMenu(self)

        # set current menu state to main menu (the string is the one you change)
        self.menu_state = "main"
        self.curr_menu = self.main_menu

        # check if the game is paused
        self.paused = False

        # set sfx and music multiplier
        self.sfx_multiplier = 0.5
        self.music_multiplier = 0.5

    def loop(self):
        while True:
            # set black BG
            self.screen.fill((16, 16, 16))

            # track cursor x,y coords
            mx, my = pygame.mouse.get_pos()

            # draw current menu's visuals (i.e. buttons,text)
            self.curr_menu.draw_screen()
            # change menu (if applicable)
            self.change_menu()

            if self.popUp.minor:
                self.popUp.draw_screen()

            for event in pygame.event.get():
                # click X button to quit
                if event.type == MINOREVENT:
                    if not self.popUp.minor:
                        self.popUp = Popup(self)
                    self.popUp.minor = True
                if event.type == pygame.QUIT:
                    pygame.quit()

                self.popUp.catch_actions(event, mx, my)
                # catch current menu's actions (i.e. mouse click)
                self.curr_menu.catch_actions(event, mx, my)

            # keep updating display
            pygame.display.update()

    def change_menu(self):
        # if inner menu state is MainMenu
        prev_state = self.curr_menu
        if self.menu_state == "main":
            self.curr_menu = self.main_menu
        # if inner menu state is OptionsMenu
        elif self.menu_state == "options":
            self.curr_menu = self.options_menu
        # if inner menu state is OptionsMenu
        elif self.menu_state == "play":
            self.curr_menu = self.gameplay
            self.paused = False
        # if inner menu state is PauseMenu
        elif self.menu_state == "pause":
            self.curr_menu = self.pause_menu
            self.paused = True

        # if inner menu state is LoadMenu
        elif self.menu_state == "load":
            self.curr_menu = self.load_menu
        # if inner menu state is SaveConfirmation
        elif self.menu_state == "save_confirm":
            self.curr_menu = self.save_confirmation
            self.paused = True
        # if inner menu state is SaveConfirmation
        elif self.menu_state == "save":
            self.curr_menu = self.save_menu
            self.paused = True


game = Game()
while True:
    game.loop()
