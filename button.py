import pygame
from pygame.locals import *
from colors import *
from text import *
import os


class Button:
    def __init__(self, x, y, width, height, color, clicked, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clicked = clicked
        self.game = game

        self.click_down = pygame.mixer.Sound('assets/menu_down.wav')
        self.click_up = pygame.mixer.Sound('assets/menu_up.wav')

    def draw(self, screen):
        # draw rectangle on screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

    def draw_volume(self, screen, vol, multiplier):
        if vol == "sfx":
            if self.game.sfx_multiplier >= multiplier:
                self.color = GREEN
        if vol == "music":
            if self.game.music_multiplier >= multiplier:
                self.color = GREEN
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

    def hovers(self, mx, my):
        # if mouse is over button
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.height:
                return True
        return False

    def change_menu(self, event, mx, my, state):
        # if left click
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # sfx
                self.click_down.play()
                # set button dark (currently clicked)
                self.color = DARK_GRAY
                # self reference of if it's clicked
                self.clicked = True

        # if left click lifted
        if event.type == MOUSEBUTTONUP and event.button == 1:
            # if self reference clicked is TRUE
            if self.clicked:
                # if mouse currently above button
                if self.hovers(mx, my):
                    # sfx
                    self.click_up.play()
                    # change inner menu state
                    self.game.menu_state = state

                    # if saving game
                    if state == "save":
                        self.saveGame()
                    # if loading game
                    elif state == "load":
                        self.loadGame()

                # now unclicked
                self.clicked = False
                # clicked button turns light gray (unselected)
                self.color = LIGHT_GRAY

        # mouse movement action
        if event.type == MOUSEMOTION:
            # if mouse currently above button
            if self.hovers(mx, my):
                # if just hovering (no click), turn gray
                if not self.clicked:
                    self.color = GRAY
                # if hovering AND clicked, turn dark gray (selected)
                else:
                    self.color = DARK_GRAY
            # untouched buttons should always be gray
            else:
                self.color = LIGHT_GRAY

    def change_difficulty(self, event, mx, my, difficulty, button1, button2):
        # if left click
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # make sure the difficulty isn't already set
                if self.game.difficulty != difficulty:
                    # sfx
                    self.click_down.play()
                    # set button dark (currently clicked)
                    self.color = DARK_GRAY
                    # self reference of if it's clicked
                    self.clicked = True

        # if left click lifted
        if event.type == MOUSEBUTTONUP and event.button == 1:
            # if self reference clicked is TRUE
            if self.clicked:
                # if mouse currently above button
                if self.hovers(mx, my):
                    # make sure the difficulty isn't already set
                    if self.game.difficulty != difficulty:
                        # sfx
                        self.click_up.play()
                        # change inner difficulty state
                        self.game.difficulty = difficulty
                # now unclicked
                self.clicked = False
                # Unselect the other two difficulty buttons
                button1.color = LIGHT_GRAY
                button2.color = LIGHT_GRAY

        # mouse movement action
        if event.type == MOUSEMOTION:
            # if mouse currently above button
            if self.hovers(mx, my):
                # if just hovering (no click), turn gray
                if not self.clicked:
                    self.color = GRAY
                # if hovering AND clicked, turn dark gray (selected)
                else:
                    self.color = DARK_GRAY
            # untouched buttons should always be gray
            else:
                self.color = LIGHT_GRAY

    def save(self, event, mx, my):
        # if left click
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # sfx
                self.click_down.play()
                # set button dark (currently clicked)
                self.color = DARK_GRAY
                # self reference of if it's clicked
                self.clicked = True

        # if left click lifted
        if event.type == MOUSEBUTTONUP and event.button == 1:
            # if self reference clicked is TRUE
            if self.clicked:
                # if mouse currently above button
                if self.hovers(mx, my):
                    # sfx
                    self.click_up.play()
                    # change inner difficulty state
                    pygame.quit()

        # mouse movement action
        if event.type == MOUSEMOTION:
            # if mouse currently above button
            if self.hovers(mx, my):
                # if just hovering (no click), turn gray
                if not self.clicked:
                    self.color = GRAY
                # if hovering AND clicked, turn dark gray (selected)
                else:
                    self.color = DARK_GRAY
            # untouched buttons should always be gray
            else:
                self.color = LIGHT_GRAY

    def quit(self, event, mx, my):
        # if left click
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # sfx
                self.click_down.play()
                # set button dark (currently clicked)
                self.color = DARK_GRAY
                # self reference of if it's clicked
                self.clicked = True

        # if left click lifted
        if event.type == MOUSEBUTTONUP and event.button == 1:
            # if self reference clicked is TRUE
            if self.clicked:
                # if mouse currently above button
                if self.hovers(mx, my):
                    # sfx
                    self.click_up.play()
                    # change inner difficulty state
                    pygame.quit()

        # mouse movement action
        if event.type == MOUSEMOTION:
            # if mouse currently above button
            if self.hovers(mx, my):
                # if just hovering (no click), turn gray
                if not self.clicked:
                    self.color = GRAY
                # if hovering AND clicked, turn dark gray (selected)
                else:
                    self.color = DARK_GRAY
            # untouched buttons should always be gray
            else:
                self.color = LIGHT_GRAY

    def change_volume(self, event, mx, my, vol, multiplier):
        # if left click
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # sfx
                self.click_down.play()
                # set button dark (currently clicked)
                self.color = DARK_GRAY
                # change sfx volume
                if vol == "sfx":
                    self.game.sfx_multiplier = multiplier
                # change music volume
                elif vol == "music":
                    self.game.music_multiplier = multiplier

        # mouse movement action
        if event.type == MOUSEMOTION:
            # if mouse currently above button
            if self.hovers(mx, my):
                # if just hovering (no click), turn gray
                if not self.clicked:
                    self.color = GRAY
                # if hovering AND clicked, turn dark gray (selected)
                else:
                    self.color = DARK_GRAY
            # untouched buttons should always be gray
            else:
                self.color = LIGHT_GRAY

    def change_ui(self, event, mx, my, menu, change):
        # if left click
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # sfx
                self.click_down.play()

                if menu == "gameplay":
                    if self.game.button_selected != change:
                        if change == "health":
                            self.game.button_selected = "health"
                        elif change == "stats":
                            self.game.button_selected = "stats"
                        elif change == "pitstop":
                            # change inner menu state
                            self.game.menu_state = "pitstop"
                elif menu == "pitstop":
                    if self.game.pitstop_menu != change:
                        if change == "party":
                            self.game.pitstop_menu = "party"
                        elif change == "supplies":
                            self.game.pitstop_menu = "supplies"

    def saveGame(self):
        f = open("save.txt", "w")

        # settings
        f.write("difficulty=" + str(self.game.difficulty) + "\n")
        f.write("sfx=" + str(self.game.sfx_multiplier) + "\n")
        f.write("music=" + str(self.game.music_multiplier) + "\n")
        # healths
        f.write("alive=" + str(self.game.alive) + "\n")
        f.write("u1_health=" + str(self.game.u1_health) + "\n")
        f.write("u2_health=" + str(self.game.u2_health) + "\n")
        f.write("u3_health=" + str(self.game.u3_health) + "\n")
        f.write("u4_health=" + str(self.game.u4_health) + "\n")
        # stats
        f.write("traveled=" + str(self.game.traveled) + "\n")
        f.write("miles_left=" + str(self.game.miles_left) + "\n")
        # supplies
        f.write("fuel=" + str(self.game.fuel) + "\n")
        f.write("food=" + str(self.game.food) + "\n")
        f.write("money=" + str(self.game.money) + "\n")

        f.close()

    def loadGame(self):
        # make sure that txt file is not empty
        if os.stat("save.txt").st_size != 0:
            f = open("save.txt", "r")

            # load difficulty
            lines = f.read().split("\n")
            lines.pop()
            for i in lines:
                string = i.split("=")
                # settings
                if string[0] == "difficulty":
                    self.game.difficulty = string[1]
                elif string[0] == "sfx":
                    self.game.sfx_multiplier = float(string[1])
                elif string[0] == "music":
                    self.game.music_multiplier = float(string[1])
                # healths
                elif string[0] == "alive":
                    self.game.alive = int(string[1])
                elif string[0] == "u1_health":
                    self.game.u1_health = int(string[1])
                elif string[0] == "u2_health":
                    self.game.u2_health = int(string[1])
                elif string[0] == "u3_health":
                    self.game.u3_health = int(string[1])
                elif string[0] == "u4_health":
                    self.game.u4_health = int(string[1])
                # stats
                elif string[0] == "traveled":
                    self.game.traveled = int(string[1])
                elif string[0] == "miles_left":
                    self.game.miles_left = int(string[1])
                # supplies
                elif string[0] == "fuel":
                    self.game.fuel = int(string[1])
                elif string[0] == "food":
                    self.game.food = int(string[1])
                elif string[0] == "money":
                    self.game.money = int(string[1])

            f.close()

    def medkit(self, event, mx, my, text):
        # heal lowest health person -> change item system later on
        # prevents using a medkit if everyone is already fully healed or that there is no medkit anymore
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # if mouse is above button
            if self.hovers(mx, my):
                # sfx
                self.click_down.play()
                healtharr = [self.game.u1_health, self.game.u2_health, self.game.u3_health, self.game.u4_health]
                if min(healtharr) != 100:
                    lowest_heath_index = healtharr.index(min(healtharr))
                    self.game.medkits -=1
                    text.text = "Medkit: " + str(self.game.medkits)
                    if lowest_heath_index == 0:
                        if self.game.u1_health > 80:
                            self.game.u1_health = 100
                        else:
                            self.game.u1_health += 20
                    if lowest_heath_index == 1:
                        if self.game.u2_health > 80:
                            self.game.u2_health = 100
                        else:
                            self.game.u2_health += 20
                    if lowest_heath_index == 2:
                        if self.game.u3_health > 80:
                            self.game.u3_health = 100
                        else:
                            self.game.u3_health += 20
                    if lowest_heath_index == 3:
                        if self.game.u4_health > 80:
                            self.game.u4_health = 100
                        else:
                            self.game.u4_health += 20

                pygame.display.update()
