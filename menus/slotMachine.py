import pygame
import numpy as np
from colors import *

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
bananaimg = pygame.transform.scale(bananaimg, (130, 140))

cherryimg = pygame.image.load('assets/Cherry.png')
cherryimg = pygame.transform.scale(cherryimg, (130, 140))

diamondimg = pygame.image.load('assets/Diamond.png')
diamondimg = pygame.transform.scale(diamondimg, (130, 140))

grapeimg = pygame.image.load('assets/Grapes.png')
grapeimg = pygame.transform.scale(grapeimg, (130, 140))

jackpotimg = pygame.image.load('assets/7.png')
jackpotimg = pygame.transform.scale(jackpotimg, (130, 140))

icon_dict = {"Jackpot-7": jackpotimg, "Bananas": bananaimg, "Cherry": cherryimg, "Diamond": diamondimg, "Grapes": grapeimg}

class IconLocation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        self.image = pygame.image.load("assets/"+icon+".png")
        self.image = pygame.transform.scale(self.image, (130,140))

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
        self.first = IconLocation(880, 90, "Bananas")
        self.second = IconLocation(880, 200, "Cherry")
        self.third = IconLocation(880, 310, "Grapes")
        self.fourth = IconLocation(880, 420, "Diamond")
        self.fifth = IconLocation(880, 530, "7")
        self.Location_menu = pygame.sprite.Group()
        self.Location_menu.add(self.first)
        self.Location_menu.add(self.second)
        self.Location_menu.add(self.third)
        self.Location_menu.add(self.fourth)
        self.Location_menu.add(self.fifth)

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

        self.game.screen.blit(pc.render("Total "+str(self.game.money)+"$", True, WHITE), (970, 30))

        # Print menu reward for each icon
        screen.blit(pu.render("X 3  + 30$", True, WHITE), (1050, 140))
        screen.blit(pu.render("X 3  + 35$", True, WHITE), (1050, 260))
        screen.blit(pu.render("X 3  + 30$", True, WHITE), (1050, 380))
        screen.blit(pu.render("X 3  + 60$", True, WHITE), (1050, 500))
        screen.blit(pu.render("X 3  + 100$", True, WHITE), (1050, 620))
        self.Location_menu.draw(self.game.screen)

        pygame.display.flip()

    def catch_actions(self, event, mx, my):
        # press esc key to go back to PITSOP
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.menu_state = "pitstop"

        # left click to play new game
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 1 click = 1 try ====> -5$
            if self.total_cash >= 5:
                self.total_cash -= 5
                self.game.money -= 5
                self.newGame()