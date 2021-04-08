import pygame
from pygame.locals import *
from colors import *
from text import *
import os

class Healthbar:
    def __init__(self, game, x, y, player):
        self.game = game
        self.x = x
        self.y = y
        self.player = player

    def draw(self, screen):
        if self.player == "car":
            ct = 0
            for i in range(int(self.game.car_health/10)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
        elif self.player == "u1":
            ct = 0
            for i in range(int(self.game.u1_health/10)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
        elif self.player == "u2":
            ct = 0
            for i in range(int(self.game.u2_health/10)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
        elif self.player == "u3":
            ct = 0
            for i in range(int(self.game.u3_health/10)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
        elif self.player == "u4":
            ct = 0
            for i in range(int(self.game.u4_health/10)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
