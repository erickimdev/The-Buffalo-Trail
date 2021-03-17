import types
import pygame
from pygame.locals import *
from button import *
from text import *

pygame.init()
click_down = pygame.mixer.Sound('assets/menu_down.wav')
click_up = pygame.mixer.Sound('assets/menu_up.wav')
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Buffalo Trail - Created by Pythoneers")
sfx_list = [type(Button), type(Button), type(Button), type(Button), type(Button),
            type(Button), type(Button), type(Button), type(Button), type(Button)]
music_list = [type(Button), type(Button), type(Button), type(Button), type(Button),
              type(Button), type(Button), type(Button), type(Button), type(Button)]
sfx_volume = 1
music_volume = 1
first_time_options = True
interact_text = type(Text)

def main_menu():
    # Instantiate game title header
    title_y = 135
    the_buffalo = Text('THE   BUFFA LO', width / 2, title_y, 125, (255, 255, 255))
    trail = Text('TRAIL', width / 2, title_y + 95, 125, (255, 255, 255))

    # Instantiate PLAY GAME button
    play_button = Button(300, 575, 275, 100, (192, 192, 192), False, play)
    play_button_text = Text('PLAY GAME', 440, 628, 50, (0, 0, 0))

    # Instantiate OPTIONS button
    options_button = Button(800, 575, 250, 100, (192, 192, 192), False, options)
    options_button_text = Text('OPTIONS', 928, 628, 50, (0, 0, 0))

    while True:
        # Set black BG
        screen.fill((16, 16, 16))
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
            play_button.click_button(event, mx, my)
            # Catch OPTIONS button clicks
            options_button.click_button(event, mx, my)

        pygame.display.update()


def update_sfx_1():
    sfx_list[0].sfx_multiplier = .1

    for i in range(1):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(1, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_2():
    sfx_list[1].sfx_multiplier = .2

    for i in range(2):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(2, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_3():
    sfx_list[2].sfx_multiplier = .3

    for i in range(3):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(3, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_4():
    sfx_list[3].sfx_multiplier = .4

    for i in range(4):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(4, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_5():
    sfx_list[4].sfx_multiplier = .5

    for i in range(5):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(5, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_6():
    sfx_list[5].sfx_multiplier = .6

    for i in range(6):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(6, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_7():
    sfx_list[6].sfx_multiplier = .7

    for i in range(7):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(7, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_8():
    sfx_list[7].sfx_multiplier = .8

    for i in range(8):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(8, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_9():
    sfx_list[8].sfx_multiplier = .9

    for i in range(9):
        sfx_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(9, len(sfx_list)):
        sfx_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_sfx_10():
    sfx_list[9].sfx_multiplier = 1

    for i in range(10):
        sfx_list[i].color = (0x27, 0x80, 0x1F)

    pygame.display.update()


def update_music_1():
    music_list[0].music_multiplier = .1

    for i in range(1):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(1, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_2():
    music_list[1].music_multiplier = .2

    for i in range(2):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(2, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_3():
    music_list[2].music_multiplier = .3

    for i in range(3):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(3, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_4():
    music_list[3].music_multiplier = .4

    for i in range(4):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(4, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_5():
    music_list[4].music_multiplier = .5

    for i in range(5):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(5, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_6():
    music_list[5].music_multiplier = .6

    for i in range(6):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(6, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_7():
    music_list[6].music_multiplier = .7

    for i in range(7):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(7, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_8():
    music_list[7].music_multiplier = .8

    for i in range(8):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(8, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_9():
    music_list[8].music_multiplier = .9

    for i in range(9):
        music_list[i].color = (0x27, 0x80, 0x1F)
    for x in range(9, len(music_list)):
        music_list[x].color = (0xC4, 0xC4, 0xC4)

    pygame.display.update()


def update_music_10():
    music_list[9].music_multiplier = 1

    for i in range(10):
        music_list[i].color = (0x27, 0x80, 0x1F)

    pygame.display.update()


def update_interact():
    global interact_text
    check_key = True
    while check_key:
        for event in  pygame.event.get(pygame.KEYDOWN):
            interact_text.text = pygame.key.name(event.key).upper()
            check_key = False
    pygame.display.update()


def options():
    options_header = Text('Options', width / 2, 80, 125, (255, 255, 255))

    sfx = Text('SFX', 105, 250, 80, (255, 255, 255))
    music = Text('Music', 150, 450, 80, (255, 255, 255))

    global first_time_options
    if first_time_options:
        sfx_volume_1 = Button(300, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_1)
        sfx_volume_2 = Button(340, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_2)
        sfx_volume_3 = Button(380, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_3)
        sfx_volume_4 = Button(420, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_4)
        sfx_volume_5 = Button(460, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_5)
        sfx_volume_6 = Button(500, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_6)
        sfx_volume_7 = Button(540, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_7)
        sfx_volume_8 = Button(580, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_8)
        sfx_volume_9 = Button(620, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_9)
        sfx_volume_10 = Button(660, 200, 30, 100, (0x27, 0x80, 0x1F), False, update_sfx_10)

        sfx_list[0] = sfx_volume_1
        sfx_list[1] = sfx_volume_2
        sfx_list[2] = sfx_volume_3
        sfx_list[3] = sfx_volume_4
        sfx_list[4] = sfx_volume_5
        sfx_list[5] = sfx_volume_6
        sfx_list[6] = sfx_volume_7
        sfx_list[7] = sfx_volume_8
        sfx_list[8] = sfx_volume_9
        sfx_list[9] = sfx_volume_10

        music_volume_1 = Button(300, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_1)
        music_volume_2 = Button(340, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_2)
        music_volume_3 = Button(380, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_3)
        music_volume_4 = Button(420, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_4)
        music_volume_5 = Button(460, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_5)
        music_volume_6 = Button(500, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_6)
        music_volume_7 = Button(540, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_7)
        music_volume_8 = Button(580, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_8)
        music_volume_9 = Button(620, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_9)
        music_volume_10 = Button(660, 400, 30, 100, (0x27, 0x80, 0x1F), False, update_music_10)

        music_list[0] = music_volume_1
        music_list[1] = music_volume_2
        music_list[2] = music_volume_3
        music_list[3] = music_volume_4
        music_list[4] = music_volume_5
        music_list[5] = music_volume_6
        music_list[6] = music_volume_7
        music_list[7] = music_volume_8
        music_list[8] = music_volume_9
        music_list[9] = music_volume_10
    else:
        sfx_volume_1 = sfx_list[0]
        sfx_volume_2 = sfx_list[1]
        sfx_volume_3 = sfx_list[2]
        sfx_volume_4 = sfx_list[3]
        sfx_volume_5 = sfx_list[4]
        sfx_volume_6 = sfx_list[5]
        sfx_volume_7 = sfx_list[6]
        sfx_volume_8 = sfx_list[7]
        sfx_volume_9 = sfx_list[8]
        sfx_volume_10 = sfx_list[9]

        music_volume_1 = music_list[0]
        music_volume_2 = music_list[1]
        music_volume_3 = music_list[2]
        music_volume_4 = music_list[3]
        music_volume_5 = music_list[4]
        music_volume_6 = music_list[5]
        music_volume_7 = music_list[6]
        music_volume_8 = music_list[7]
        music_volume_9 = music_list[8]
        music_volume_10 = music_list[9]

    # Controls
    controls = Text("Controls", 210, 600, 80, (255, 255, 255))
    interact = Text('Interact', 600, 600, 80, (255, 255, 255))
    global interact_text
    if first_time_options:
        interact_input = Text("E", 900, 600, 80, (0, 0, 0))
        interact_text = interact_input

    interact_input = interact_text
    interact_button = Button(875, 575, 50, 50, (255, 255, 255), False, update_interact)
    first_time_options = False
    in_options = True
    while in_options:
        # Set black BG
        screen.fill((16, 16, 16))

        # Write OPTIONS header
        options_header.draw(screen)

        # SFX
        sfx.draw(screen)
        sfx_volume_1.draw(screen)
        sfx_volume_2.draw(screen)
        sfx_volume_3.draw(screen)
        sfx_volume_4.draw(screen)
        sfx_volume_5.draw(screen)
        sfx_volume_6.draw(screen)
        sfx_volume_7.draw(screen)
        sfx_volume_8.draw(screen)
        sfx_volume_9.draw(screen)
        sfx_volume_10.draw(screen)

        # music
        music.draw(screen)
        music_volume_1.draw(screen)
        music_volume_2.draw(screen)
        music_volume_3.draw(screen)
        music_volume_4.draw(screen)
        music_volume_5.draw(screen)
        music_volume_6.draw(screen)
        music_volume_7.draw(screen)
        music_volume_8.draw(screen)
        music_volume_9.draw(screen)
        music_volume_10.draw(screen)

        controls.draw(screen)
        interact.draw(screen)
        interact_button.draw(screen)
        interact_input.draw(screen)

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Click X button to quit
            if event.type == pygame.QUIT:
                pygame.quit()
            # Press right button to go back to previous menu
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                in_options = False

            sfx_volume_1.click_button(event, mx, my)
            sfx_volume_2.click_button(event, mx, my)
            sfx_volume_3.click_button(event, mx, my)
            sfx_volume_4.click_button(event, mx, my)
            sfx_volume_5.click_button(event, mx, my)
            sfx_volume_6.click_button(event, mx, my)
            sfx_volume_7.click_button(event, mx, my)
            sfx_volume_8.click_button(event, mx, my)
            sfx_volume_9.click_button(event, mx, my)
            sfx_volume_10.click_button(event, mx, my)

            music_volume_1.click_button(event, mx, my)
            music_volume_2.click_button(event, mx, my)
            music_volume_3.click_button(event, mx, my)
            music_volume_4.click_button(event, mx, my)
            music_volume_5.click_button(event, mx, my)
            music_volume_6.click_button(event, mx, my)
            music_volume_7.click_button(event, mx, my)
            music_volume_8.click_button(event, mx, my)
            music_volume_9.click_button(event, mx, my)
            music_volume_10.click_button(event, mx, my)

            interact_button.click_button(event, mx, my)

        pygame.display.update()


def play():
    playing = True
    while playing:
        # Set black BG
        screen.fill((16, 16, 16))
        mx, my = pygame.mouse.get_pos()
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
