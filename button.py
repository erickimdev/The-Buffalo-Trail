import pygame
from pygame.locals import *


class Button:

    def __init__(self, x, y, width, height, color, clicked, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clicked = clicked
        self.function = function
        self.changed = False
        self.previous_color = color
        self.sfx_multiplier = 1.0
        self.music_multiplier = 1.0

    def set_function(self, function):
        self.function = function

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

    def hovers(self, mx, my):
        # If mouse is over button
        if self.x < mx < self.x + self.width:
            if self.y < my < self.y + self.height:
                return True
        return False

    def click_button(self, event, mx, my):
        # Import click sfx
        click_down = pygame.mixer.Sound('assets/menu_down.wav')
        click_up = pygame.mixer.Sound('assets/menu_up.wav')
        click_up.set_volume(self.sfx_multiplier)
        click_down.set_volume(self.sfx_multiplier)

        red, blue, green = self.color
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.hovers(mx, my):
                click_down.play()
                self.color = (red - 30, blue - 30, green - 30)
                self.clicked = True

        if event.type == MOUSEBUTTONUP and event.button == 1:
            if self.clicked:
                if self.hovers(mx, my):
                    click_up.play()
                    self.color = self.previous_color
                    self.function()
                self.clicked = False

        # if event.type == MOUSEMOTION:
        #     if self.hovers(mx, my):
        #         if not self.changed:
        #             self.previous_color = self.color
        #             if not self.clicked:
        #                 self.color = (red + 30, blue + 30, green + 30)
        #             else:
        #                 self.color = (red - 30, blue - 30, green - 30)
        #             self.changed = True
        #         else:
        #             self.color = self.previous_color
        #             self.changed = False
        #     else:
        #         self.color = self.previous_color
