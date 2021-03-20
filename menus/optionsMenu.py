import pygame
from text import *
from button import *

class OptionsMenu:
    def __init__(self, game):
        self.game = game

        # instantiate OPTIONS header
        self.options_header = Text('OPTIONS', self.game.width/2, 90, 70, WHITE)

        x = 900
        y = 300
        # instantiate SFX text
        self.sfxText = Text('SFX', 168, y+30, 40, (255, 255, 255))
        # instantiate Music test
        self.musicText = Text('Music', 150, y+170, 40, (255, 255, 255))

        # instantiate DIFFICULTY text
        self.difficultyText = Text('Difficulty', x+92, y-42, 40, WHITE)
        # instantiate EASY button
        self.easy_button = Button(x, y, 200, 60, LIGHT_GRAY, False, self.game)
        self.easy_button_text = Text('Easy', x+100, y+30, 30, BLACK)
        # instantiate MEDIUM button
        self.medium_button = Button(x, y+80, 200, 60, LIGHT_GRAY, False, self.game)
        self.medium_button_text = Text('Medium', x+100, y+110, 30, BLACK)
        # instantiate HARD button
        self.hard_button = Button(x, y+160, 200, 60, LIGHT_GRAY, False, self.game)
        self.hard_button_text = Text('Hard', x+100, y+190, 30, BLACK)

        # SFX buttons
        self.sfx_volume_1 = Button(300,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_2 = Button(340,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_3 = Button(380,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_4 = Button(420,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_5 = Button(460,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_6 = Button(500,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_7 = Button(540,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_8 = Button(580,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_9 = Button(620,  273, 30, 100, GREEN, False, self.game)
        self.sfx_volume_10 = Button(660, 273, 30, 100, GREEN, False, self.game)
        # Music volume buttons
        self.music_volume_1 = Button(300,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_2 = Button(340,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_3 = Button(380,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_4 = Button(420,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_5 = Button(460,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_6 = Button(500,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_7 = Button(540,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_8 = Button(580,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_9 = Button(620,  420, 30, 100, GREEN, False, self.game)
        self.music_volume_10 = Button(660, 420, 30, 100, GREEN, False, self.game)

    def draw_screen(self):
        # draw OPTIONS header
        self.options_header.draw(self.game.screen)
        # draw SFX text
        self.sfxText.draw(self.game.screen)
        # draw Music text
        self.musicText.draw(self.game.screen)
        # draw DIFFICULTY text
        self.difficultyText.draw(self.game.screen)

        # shade current difficulty button
        if self.game.difficulty == "easy":
            self.easy_button.color = DARK_GRAY
        elif self.game.difficulty == "medium":
            self.medium_button.color = DARK_GRAY
        elif self.game.difficulty == "hard":
            self.hard_button.color = DARK_GRAY

        # draw buttons
        # EASY button
        self.easy_button.draw(self.game.screen)
        self.easy_button_text.draw(self.game.screen)
        # MEDIUM button
        self.medium_button.draw(self.game.screen)
        self.medium_button_text.draw(self.game.screen)
        # HARD button
        self.hard_button.draw(self.game.screen)
        self.hard_button_text.draw(self.game.screen)

        # draw SFX buttons
        self.sfx_volume_1.draw_volume(self.game.screen, "sfx", 0.1)
        self.sfx_volume_2.draw_volume(self.game.screen, "sfx", 0.2)
        self.sfx_volume_3.draw_volume(self.game.screen, "sfx", 0.3)
        self.sfx_volume_4.draw_volume(self.game.screen, "sfx", 0.4)
        self.sfx_volume_5.draw_volume(self.game.screen, "sfx", 0.5)
        self.sfx_volume_6.draw_volume(self.game.screen, "sfx", 0.6)
        self.sfx_volume_7.draw_volume(self.game.screen, "sfx", 0.7)
        self.sfx_volume_8.draw_volume(self.game.screen, "sfx", 0.8)
        self.sfx_volume_9.draw_volume(self.game.screen, "sfx", 0.9)
        self.sfx_volume_10.draw_volume(self.game.screen, "sfx", 1.0)
        # draw Music volume buttons
        self.music_volume_1.draw_volume(self.game.screen, "music", 0.1)
        self.music_volume_2.draw_volume(self.game.screen, "music", 0.2)
        self.music_volume_3.draw_volume(self.game.screen, "music", 0.3)
        self.music_volume_4.draw_volume(self.game.screen, "music", 0.4)
        self.music_volume_5.draw_volume(self.game.screen, "music", 0.5)
        self.music_volume_6.draw_volume(self.game.screen, "music", 0.6)
        self.music_volume_7.draw_volume(self.game.screen, "music", 0.7)
        self.music_volume_8.draw_volume(self.game.screen, "music", 0.8)
        self.music_volume_9.draw_volume(self.game.screen, "music", 0.9)
        self.music_volume_10.draw_volume(self.game.screen, "music", 1.0)

    def catch_actions(self, event, mx, my):
        # right click/ESC key goes to MainMenu OR PauseMenu
        if (event.type == MOUSEBUTTONDOWN and event.button == 3) \
                or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            # if Options clicked from main menu ONLY
            if not self.game.paused:
                self.game.menu_state = "main"
            elif self.game.paused:
                self.game.menu_state = "pause"

        # catch difficulty changes
        self.easy_button.change_difficulty(event, mx, my, "easy", self.medium_button, self.hard_button)
        self.medium_button.change_difficulty(event, mx, my, "medium", self.easy_button, self.hard_button)
        self.hard_button.change_difficulty(event, mx, my, "hard", self.easy_button, self.medium_button)

        # catch SFX volume changes
        self.sfx_volume_1.change_volume(event, mx, my, "sfx", 0.1)
        self.sfx_volume_2.change_volume(event, mx, my, "sfx", 0.2)
        self.sfx_volume_3.change_volume(event, mx, my, "sfx", 0.3)
        self.sfx_volume_4.change_volume(event, mx, my, "sfx", 0.4)
        self.sfx_volume_5.change_volume(event, mx, my, "sfx", 0.5)
        self.sfx_volume_6.change_volume(event, mx, my, "sfx", 0.6)
        self.sfx_volume_7.change_volume(event, mx, my, "sfx", 0.7)
        self.sfx_volume_8.change_volume(event, mx, my, "sfx", 0.8)
        self.sfx_volume_9.change_volume(event, mx, my, "sfx", 0.9)
        self.sfx_volume_10.change_volume(event, mx, my, "sfx", 1.0)
        # catch music volume changes
        self.music_volume_1.change_volume(event, mx, my, "music", 0.1)
        self.music_volume_2.change_volume(event, mx, my, "music", 0.2)
        self.music_volume_3.change_volume(event, mx, my, "music", 0.3)
        self.music_volume_4.change_volume(event, mx, my, "music", 0.4)
        self.music_volume_5.change_volume(event, mx, my, "music", 0.5)
        self.music_volume_6.change_volume(event, mx, my, "music", 0.6)
        self.music_volume_7.change_volume(event, mx, my, "music", 0.7)
        self.music_volume_8.change_volume(event, mx, my, "music", 0.8)
        self.music_volume_9.change_volume(event, mx, my, "music", 0.9)
        self.music_volume_10.change_volume(event, mx, my, "music", 1.0)