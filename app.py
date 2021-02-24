import pygame
from pygame.locals import *
from button import *
from text import *

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Buffalo Trail - Created by Pythoneers")

def main_menu():
    # Instantiate game title header
    title_y = 135
    the_buffalo = Text('THE   BUFFA LO', width/2, title_y, 125, (255,255,255))
    trail = Text('TRAIL', width/2, title_y+95, 125, (255,255,255))

    # Instantiate PLAY GAME button
    play_button = Button(300, 575, 275, 100, (192, 192, 192), False, play)
    play_button_text = Text('PLAY GAME', 440, 628, 50, (0,0,0))

    # Instantiate OPTIONS button
    options_button = Button(800, 575, 250, 100, (192, 192, 192), False, options)
    options_button_text = Text('OPTIONS', 928, 628, 50, (0,0,0))

    while True:
        # Set black BG
        screen.fill((16,16,16))
        # Draw game name
        the_buffalo.draw(screen)
        trail.draw(screen)
        # Draw buttons
            # PLAY GAME button
        play_button.draw(screen)
        play_button_text.draw(screen)
            # OPTIONS button
        options_button.draw(screen)
        options_button_text.draw(screen)

        # Track cursor x,y coords
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Click X button to quit
            if event.type == pygame.QUIT:
                pygame.quit()
            # Press esc key to quit
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()

            # Catch PLAY button clicks
            play_button.click_button(event,mx,my)
            # Catch OPTIONS button clicks
            options_button.click_button(event,mx,my)

        pygame.display.update()

def options():
    options_header = Text('Options', width/2, 80, 125, (255,255,255))

    in_options = True
    while in_options:
        # Set black BG
        screen.fill((16,16,16))

        # Write OPTIONS header
        options_header.draw(screen)

        for event in pygame.event.get():
            # Click X button to quit
            if event.type == pygame.QUIT:
                pygame.quit()
            # Press right button to go back to previous menu
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                in_options = False

        pygame.display.update()

def play():
    playing = True
    while playing:
        # Set black BG
        screen.fill((16,16,16))

        for event in pygame.event.get():
            # Click X button to quit
            if event.type == pygame.QUIT:
                pygame.quit()
            # Press right button to go back to previous menu
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                playing = False

        pygame.time.Clock().tick(30)
        pygame.display.update()

main_menu()