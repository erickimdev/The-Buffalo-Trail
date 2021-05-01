import pygame
from pygame.locals import *
from colors import *
from text import *

class Healthbar:
    def __init__(self, game, x, y, player):
        self.game = game
        self.x = x
        self.y = y
        self.player = player
        self.carHealth_text = Text('{}%'.format(self.game.car_health * 10), self.x+155, self.y+17, 20, WHITE)
        self.u1Health_text = Text('{}%'.format(self.game.u1_health * 10), self.x+155, self.y+17, 20, WHITE)
        self.u2Health_text = Text('{}%'.format(self.game.u2_health * 10), self.x+155, self.y+17, 20, WHITE)
        self.u3Health_text = Text('{}%'.format(self.game.u3_health * 10), self.x+155, self.y+17, 20, WHITE)
        self.u4Health_text = Text('{}%'.format(self.game.u4_health * 10), self.x+155, self.y+17, 20, WHITE)

    def draw_rectangle(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x,     self.y,    300, 2), 0)
        pygame.draw.rect(screen, WHITE, (self.x,     self.y+30, 300, 2), 0)
        pygame.draw.rect(screen, WHITE, (self.x,     self.y,    2,   30), 0)
        pygame.draw.rect(screen, WHITE, (self.x+298, self.y,    2,   30), 0)

    def update(self):
        self.carHealth_text.text = '{}%'.format(self.game.car_health * 10)
        self.u1Health_text.text = '{}%'.format(self.game.u1_health * 10)
        self.u2Health_text.text = '{}%'.format(self.game.u2_health * 10)
        self.u3Health_text.text = '{}%'.format(self.game.u3_health * 10)
        self.u4Health_text.text = '{}%'.format(self.game.u4_health * 10)

    def draw(self, screen):
        # update healths
        self.update()

        # car
        if self.player == "car":
            ct = 0
            for i in range(int(self.game.car_health)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
            self.draw_rectangle(screen)
            self.carHealth_text.draw(screen)

        # user 1
        elif self.player == "u1":
            ct = 0
            for i in range(int(self.game.u1_health)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
            self.draw_rectangle(screen)
            self.u1Health_text.draw(screen)

        # user 2
        elif self.player == "u2":
            ct = 0
            for i in range(int(self.game.u2_health)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
            self.draw_rectangle(screen)
            self.u2Health_text.draw(screen)

        # user 3
        elif self.player == "u3":
            ct = 0
            for i in range(int(self.game.u3_health)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
            self.draw_rectangle(screen)
            self.u3Health_text.draw(screen)

        # user 4
        elif self.player == "u4":
            ct = 0
            for i in range(int(self.game.u4_health)):
                pygame.draw.rect(screen, GREEN, (self.x+(ct*30), self.y, 30, 30), 0)
                ct += 1
            self.draw_rectangle(screen)
            self.u4Health_text.draw(screen)
