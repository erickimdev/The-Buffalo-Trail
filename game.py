import pygame
from pygame.locals import *
from button import *
from text import *
from play import *
from menus import mainMenu
from menus import optionsMenu
from menus import pauseMenu
from menus import save_loadMenu
from menus import pitStop
from menus import talkToStranger
from Strangers import stranger1
from Strangers import stranger2
from Strangers import stranger3

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

               # "pit stop"
        self.Pit_Stop_menu = pitStop.PitStop(self)
            # "Talk to stranger"
        self.talk_to_stranger_menu = talkToStranger.TalkToStranger(self)
        self.Firststranger = stranger1.Stranger(self)
        self.Secondstranger = stranger2.Stranger(self)
        self.Thirdstranger = stranger3.Stranger(self) 

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

            
         # if inner menu state is Pit Stop
        elif self.menu_state == "pitStop":
            self.curr_menu = self.Pit_Stop_menu
            self.paused = True

            # if inner menu state is talkToStranger
        elif self.menu_state == "talkToStranger":
            self.curr_menu = self.talk_to_stranger_menu
            self.paused = True
        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger1":
            self.curr_menu = self.Firststranger
            self.paused = True
        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger2":
            self.curr_menu = self.Secondstranger
            self.paused = True
        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger3":
            self.curr_menu = self.Thirdstranger
            self.paused = True


game = Game()
while True:
    game.loop()