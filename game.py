import pygame
from pygame.locals import *
from button import *
from text import *
from play import *
from menus import mainMenu
from menus import optionsMenu
from menus import pauseMenu
from menus import save_loadMenu
from menus import pitstop
from menus import rest
from menus import slotMachine
from menus import blackJack
from menus import endingMenu

from menus import jobs
from menus import talkToStranger
from Strangers import stranger1
from Strangers import stranger2
from Strangers import stranger3

run = True

class Game:
    def __init__(self):
        # initialize game
        pygame.init()

        # set width/height and display screen
        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("The Buffalo Trail - Created by Pythoneers")
        self.prev_state = "pitstop"
        # set difficulty - easy, medium, hard
        self.difficulty = "medium"

        # GAMEPLAY
            # current button selected (health, stats, pitstop)
        self.button_selected = 'health'
        self.time = 5   # 0 to 24 (military time)
            # current pitstop menu (party, car, supplies)
        self.pitstop_menu = 'party'
            # car/player healths
        self.alive = 4
        self.car_health = 9
        self.u1_health = 10
        self.u2_health = 8
        self.u3_health = 5
        self.u4_health = 6
        self.medkits = 10
            # stats
        self.traveled = 0 #miles
        self.miles_left = 400 #miles
            # supplies
        self.fuel = 20 #gallons
        self.food = 500 #oz
        self.money = 1000 #dollars

        # instantiate game's menu
        self.main_menu = mainMenu.MainMenu(self) # "main"
        self.options_menu = optionsMenu.OptionsMenu(self) # "options"
        self.gameplay = Play(self) # "play"
        self.pause_menu = pauseMenu.PauseMenu(self) # "pause"
        self.load_menu = save_loadMenu.LoadMenu(self) # "load"
        self.save_confirmation = save_loadMenu.SaveMenuConfirmation(self) # "save_confirm"
        self.save_menu = save_loadMenu.SaveMenu(self) # "save"
        self.rest = rest.Rest(self) # "rest"
        self.pitstop = pitstop.PitStop(self) # "pitstop"
        self.jobs_menu = jobs.Jobs(self) # "jobs"
        self.talk_to_stranger_menu = talkToStranger.TalkToStranger(self) # "stranger"
        self.slotMachine_menu = slotMachine.SlotMachine(self) # "slotmachine"
        self.blackjack_menu = blackJack.BlackJack(self) # "blackjack"
        self.Firststranger = stranger1.Stranger(self)
        self.Secondstranger = stranger2.Stranger(self)
        self.Thirdstranger = stranger3.Stranger(self)
        self.ending_menu = endingMenu.EndingMenu(self) # "ending"

        # set current menu state to main menu (the string is the one you change)
        self.menu_state = "main"
        self.curr_menu = self.main_menu

        # check if the game is paused
        self.paused = False

        # set sfx and music multiplier
        self.sfx_multiplier = 0.5
        self.music_multiplier = 0.5

    def loop(self):
        run = True
        while run:
            # set black BG
            self.screen.fill((16,16,16))

            # track cursor x,y coords
            mx, my = pygame.mouse.get_pos()

            # draw current menu's visuals (i.e. buttons,text)
            self.curr_menu.draw_screen()

            # change menu (if applicable)
            self.change_menu()

            # keep updating display
            pygame.display.update()

            for event in pygame.event.get():
                # catch current menu's actions (i.e. mouse click)
                self.curr_menu.catch_actions(event, mx, my)

                # click X button to quit
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

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

        # if inner menu state is Pitstop
        elif self.menu_state == "pitstop":
            if self.prev_state == "jobs":
                self.prev_state = "pitstop"
            self.curr_menu = self.pitstop
        elif self.menu_state == "rest":
            self.curr_menu = self.rest
        elif self.menu_state == "slotmachine":
            self.curr_menu = self.slotMachine_menu
        elif self.menu_state == "blackjack":
            self.curr_menu = self.blackjack_menu

        # if inner menu state is LoadMenu
        elif self.menu_state == "load":
            self.curr_menu = self.load_menu
        # if inner menu state is SaveConfirmation
        elif self.menu_state == "save_confirm":
            self.curr_menu = self.save_confirmation
            self.paused = True
        # if inner menu state is Save
        elif self.menu_state == "save":
            self.curr_menu = self.save_menu
            self.paused = True
        elif self.menu_state == "jobs":
            if self.prev_state == "pitstop":
                self.jobs_menu = jobs.Jobs(self)
                self.prev_state = "jobs"
            self.curr_menu = self.jobs_menu

        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger":
            self.curr_menu = self.talk_to_stranger_menu
            self.paused = True
        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger1":
            self.curr_menu = self.first_stranger
            self.paused = True
        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger2":
            self.curr_menu = self.second_stranger
            self.paused = True
        # if inner menu state is talkToStranger
        elif self.menu_state == "stranger3":
            self.curr_menu = self.third_stranger
            self.paused = True

        elif self.menu_state == "ending":
            self.curr_menu = self.ending_menu

game = Game()
while True:
    game.loop()
