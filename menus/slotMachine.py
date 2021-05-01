import pygame
import numpy as np
from colors import *
from text import *
from button import *

pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slot Machine")
logo = pygame.image.load('assets/SM.png')
pygame.display.set_icon(logo)
screen.fill(DARK_GRAY)
background = pygame.image.load('assets/SM.png').convert_alpha()
background = pygame.transform.scale(background, (600, 600))
pc = pygame.font.SysFont("yo", 70)
pu = pygame.font.SysFont("yo", 45)


icons = ["Jackpot-7", "Bananas", "Cherry", "Diamond", "Grapes"]
icons_proba = [0.1, 0.25, 0.25, 0.25, 0.15]
icon_reward_dict = {"Jackpot-7": 100, "Bananas": 30, "Cherry": 35, "Diamond": 60, "Grapes": 30}

bananaimg = pygame.image.load('assets/Bananas.png')
bananaimg = pygame.transform.scale(bananaimg, (110, 110))

cherryimg = pygame.image.load('assets/Cherry.png')
cherryimg = pygame.transform.scale(cherryimg, (110, 110))

diamondimg = pygame.image.load('assets/Diamond.png')
diamondimg = pygame.transform.scale(diamondimg, (110, 110))

grapeimg = pygame.image.load('assets/Grapes.png')
grapeimg = pygame.transform.scale(grapeimg, (110, 110))

jackpotimg = pygame.image.load('assets/7.png')
jackpotimg = pygame.transform.scale(jackpotimg, (110, 110))

icon_dict = {"Jackpot-7": jackpotimg, "Bananas": bananaimg, "Cherry": cherryimg, "Diamond": diamondimg, "Grapes": grapeimg}

class IconLocation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        self.image = pygame.image.load("assets/"+icon+".png")
        self.image = pygame.transform.scale(self.image, (110, 110))

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def set_image(self, image):
        self.image = image

class SlotMachine:
    def __init__(self, game):
        self.game = game

        # Group location
        self.left = IconLocation(140, 230, "Bananas",)
        self.middle = IconLocation(290, 230, "Cherry")
        self.right = IconLocation(425, 230, "Grapes")
        self.Location = pygame.sprite.Group()
        self.Location.add(self.left)
        self.Location.add(self.middle)
        self.Location.add(self.right)

        # Group location_menu
        mult = 118
        self.first = IconLocation(850, 90, "Bananas")
        self.second = IconLocation(850, 90 + (mult*1), "Cherry")
        self.third = IconLocation(850, 90 + (mult*2), "Grapes")
        self.fourth = IconLocation(850, 90 + (mult*3), "Diamond")
        self.fifth = IconLocation(850, 90 + (mult*4), "7")
        self.Location_menu = pygame.sprite.Group()
        self.Location_menu.add(self.first)
        self.Location_menu.add(self.second)
        self.Location_menu.add(self.third)
        self.Location_menu.add(self.fourth)
        self.Location_menu.add(self.fifth)

        self.total_text = Text('Total: ${}'.format(self.game.money), 1075, 40, 30, WHITE)
        self.banana_text =  Text('X 3  + $30',  1110, 140, 30, WHITE)
        self.cherry_text =  Text('X 3  + $35',  1110, 260, 30, WHITE)
        self.grape_text =   Text('X 3  + $30',  1110, 380, 30, WHITE)
        self.diamond_text = Text('X 3  + $60',  1110, 500, 30, WHITE)
        self.seven_text =   Text('X 3  + $100', 1123, 620, 30, WHITE)

        self.total_cash = self.game.money

    def newGame(self):
        # Generate three random icon
        rand_icons = np.random.choice(icons, 3, p=icons_proba)
        # Draw the random icons on the correct location
        self.left.set_image(icon_dict[rand_icons[0]])
        self.middle.set_image(icon_dict[rand_icons[1]])
        self.right.set_image(icon_dict[rand_icons[2]])

        # Reward if there are three identical icons
        if rand_icons[0] == rand_icons[1] == rand_icons[2]:
            # Get reward from a dict
            cash = icon_reward_dict[rand_icons[0]]
            self.total_cash += cash
            self.game.money += cash

    def draw_screen(self):
        # self.game.screen.fill(DARK_GRAY)
        self.game.screen.blit((background), (50,50))
        self.Location.draw(self.game.screen)

        # draw TOTAL text
        self.total_text.text = 'Total: ${}'.format(self.game.money)
        self.total_text.draw(self.game.screen)
        # draw REWARDS text
        self.banana_text.draw(self.game.screen)
        self.cherry_text.draw(self.game.screen)
        self.grape_text.draw(self.game.screen)
        self.diamond_text.draw(self.game.screen)
        self.seven_text.draw(self.game.screen)

        self.Location_menu.draw(self.game.screen)

        pygame.display.flip()

    def catch_actions(self, event, mx, my):
        # press esc key to go back to PITSOP
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.menu_state = "pitstop"

        # left click to play new game
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 1 click = 1 try ====> -5$
            if self.game.money >= 5:
                self.total_cash -= 5
                self.game.money -= 5
                self.newGame()