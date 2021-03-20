import pygame
from pygame.locals import *
from colors import *
from text import *

class Button:
    def __init__(self, x, y, width, height, color, clicked, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clicked = clicked
        self.game = game
        self.username = ''

        self.click_down = pygame.mixer.Sound('assets/menu_down.wav')
        self.click_up = pygame.mixer.Sound('assets/menu_up.wav')

    def draw(self, screen):
        # draw rectangle on screen
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
                        f = open("save.txt", "w")

                        # save difficulty
                        difficulty = "difficulty="
                        difficulty += str(self.game.difficulty)
                        f.write(difficulty)

                        f.close()

                    # if loading game
                    elif state == "load":
                        f = open("save.txt", "r")

                        # load difficulty
                        change = f.read().split("=")
                        self.game.difficulty = change[1]

                        f.close()

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