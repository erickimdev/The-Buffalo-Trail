import pygame
import numpy as np
from colors import *

#Have to be merged to our project

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


def start():
    global total_cash
    # Generate three random icon
    rand_icons = np.random.choice(icons, 3, p=icons_proba)
    # Draw the random icons on the correct location
    left.set_image(icon_dict[rand_icons[0]])
    middle.set_image(icon_dict[rand_icons[1]])
    right.set_image(icon_dict[rand_icons[2]])

    # Reward if there are three identical icons
    if rand_icons[0] == rand_icons[1] == rand_icons[2]:
        # Get reward from a dict
        cash = icon_reward_dict[rand_icons[0]]
        total_cash += cash
   

pygame.init()
width  = 1280
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

Location = pygame.sprite.Group()
left = IconLocation(140, 230, "Bananas",)
middle = IconLocation(290, 230, "Cherry")
right = IconLocation(425, 230, "Grapes")

# Group location
Location.add(left)
Location.add(middle)
Location.add(right)

Location_menu = pygame.sprite.Group()
first = IconLocation(880, 90, "Bananas")
second = IconLocation(880, 200, "Cherry")
third = IconLocation(880, 310, "Grapes")
fourth = IconLocation(880, 420, "Diamond")
fifth = IconLocation(880, 530, "7")

# Group location_menu
Location_menu.add(first)
Location_menu.add(second)
Location_menu.add(third)
Location_menu.add(fourth)
Location_menu.add(fifth)



icons= ["Jackpot-7", "Bananas", "Cherry", "Diamond", "Grapes"]
icons_proba = [0.1, 0.25, 0.25, 0.25, 0.15]
icon_reward_dict = {"Jackpot-7": 100, "Bananas": 30, "Cherry" : 35, "Diamond":60, "Grapes": 30}

total_cash = 1000 #as of now

bananaimg = pygame.image.load('assets/Bananas.png')
bananaimg = pygame.transform.scale(bananaimg, (130, 140)) 

cherryimg = pygame.image.load('assets/Cherry.png')
cherryimg = pygame.transform.scale(cherryimg, (130, 140)) 

diamondimg = pygame.image.load('assets/Diamond.png')
diamondimg = pygame.transform.scale(diamondimg, (130, 140)) 

grapeimg =  pygame.image.load('assets/Grapes.png')
grapeimg = pygame.transform.scale(grapeimg, (130, 140)) 

jackpotimg = pygame.image.load('assets/7.png')
jackpotimg = pygame.transform.scale(jackpotimg, (130, 140)) 


icon_dict = {"Jackpot-7": jackpotimg, "Bananas":bananaimg , "Cherry" : cherryimg, "Diamond": diamondimg, "Grapes": grapeimg}




run = True
while run:
    screen.fill(DARK_GRAY)

    screen.blit((background), (50,50))
    Location.draw(screen)

    text = pc.render("Total "+str(total_cash)+"$", True, (0, 0, 0))
    screen.blit(text, (970, 30))
    # Print menu reward for each icon
    banana_menu = pu.render("X 3  + 30$", True, (0, 0, 0))
    screen.blit(banana_menu, (1050, 140))
    cherry_menu = pu.render("X 3  + 35$", True, (0, 0, 0))
    screen.blit(cherry_menu, (1050, 260))
    grapes_menu = pu.render("X 3  + 30$", True, (0, 0, 0))
    screen.blit(grapes_menu, (1050, 380))
    diamond_menu = pu.render("X 3  + 60$", True, (0, 0, 0))
    screen.blit(diamond_menu, (1050, 500))
    seven_menu = pu.render("X 3  + 100$", True, (0, 0, 0))
    screen.blit(seven_menu, (1050, 620))
    Location_menu.draw(screen)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
        
        if event.type == pygame.KEYDOWN:
            # 1 click = 1 try ====> -5$
            if total_cash >= 5:
                total_cash -= 5
                start()
