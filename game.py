import pygame
from pygame.locals import *
from button import *
from text import *
from menu import *
from play import *

class Game:
    def __init__(self):
        # initialize game
        pygame.init()

        # set width/height and display screen
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("The Buffalo Trail - Created by Pythoneers")

        # set difficulty - easy, medium, hard
        self.difficulty = "medium"

        # instantiate game's menus
        # "main"
        self.main_menu = MainMenu(self)
        # "options"
        self.options_menu = OptionsMenu(self)
        # "play"
        self.gameplay = Play(self)
        # "pause"
        self.pause_menu = PauseMenu(self)

        # set current menu to main menu
        self.curr_menu = self.main_menu
        # set current menu state to main menu (this is the one you change)
        self.menu_state = "main"

        # check if the game is paused
        self.paused = False

    def loop(self):
        while True:
            # set black BG
            self.screen.fill((16,16,16))

            # track cursor x,y coords
            mx, my = pygame.mouse.get_pos()

            # draw current menu's visuals (i.e. buttons,text)
            self.curr_menu.draw_screen()

            # change menu (if applicable)
            self.change_menu()

            for event in pygame.event.get():
                # click X button to quit
                if event.type == pygame.QUIT:
                    pygame.quit()

                # catch current menu's actions (i.e. mouse click)
                self.curr_menu.catch_actions(event, mx, my)

            # keep updating display
            pygame.display.update()

    def change_menu(self):
        # if inner menu state is MainMenu
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

game = Game()
while True:
    game.loop()