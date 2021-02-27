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

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.hovers(mx, my):
                click_down.play()
                self.color = (105, 105, 105)
                self.clicked = True
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if self.clicked:
                if self.hovers(mx, my):
                    click_up.play()
                    self.function()
                self.clicked = False
                self.color = (192, 192, 192)
        if event.type == MOUSEMOTION:
            if self.hovers(mx, my):
                if not self.clicked:
                    self.color = (128, 128, 128)
                else:
                    self.color = (105, 105, 105)
            else:
                self.color = (192, 192, 192)
