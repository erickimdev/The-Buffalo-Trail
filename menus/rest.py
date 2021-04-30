import pygame
from text import *
from button import *
from healthbar import *

class Rest:
    def __init__(self, game):
        self.game = game
        y_offset = 100

        # instantiate text
        self.game_paused = Text('Rest', self.game.width/2, y_offset, 60, WHITE)

        # instantiate time
        self.time = Text('Time: {}:00'.format(self.game.time % 24), 350, y_offset+180, 30, WHITE)
        self.rest_text = Text('How long would you like to rest?', self.game.width/2, y_offset+430, 20, WHITE)
        # hours to sleep text
        self.hours = 1
        self.hours_text = Text('{} Hour'.format(self.hours), self.game.width/2, 570, 25, WHITE)

        # usernames/healthbars
        user_x = 750
        user_y = 170
        self.car_text = Text('BMW X6', user_x, user_y, 27, WHITE)
        self.u1_text = Text('User 1', user_x, user_y+40, 27, WHITE)
        self.u2_text = Text('User 2', user_x, user_y+80, 27, WHITE)
        self.u3_text = Text('User 3', user_x, user_y+120, 27, WHITE)
        self.u4_text = Text('User 4', user_x, user_y+160, 27, WHITE)
        # health bars
        self.u1_health = Healthbar(self.game, user_x+105, user_y+23, "u1")
        self.u2_health = Healthbar(self.game, user_x+105, user_y+63, "u2")
        self.u3_health = Healthbar(self.game, user_x+105, user_y+103, "u3")
        self.u4_health = Healthbar(self.game, user_x+105, user_y+143, "u4")

        # REST and BACK buttons
        x_offset2 = 0
        y_offset2 = 610
        # instantiate REST button
        self.rest_button = Button(x_offset2+550, y_offset2, 200, 80, LIGHT_GRAY, False, self.game)
        self.rest_button_text = Text('Rest', x_offset2+650, y_offset2+43, 30, BLACK)
        # instantiate BACK button
        self.back_button = Button(x_offset2+950, y_offset2, 200, 80, LIGHT_GRAY, False, self.game)
        self.back_button_text = Text('Back', x_offset2+1050, y_offset2+43, 30, BLACK)

        # REST bar
        self.restbar = pygame.image.load('assets/restbar.png')
        self.restbar = pygame.transform.scale(self.restbar, (875, 101))
        self.restbar_toggle = pygame.image.load('assets/restbar_toggle.png')
        self.restbar_toggle = pygame.transform.scale(self.restbar_toggle, (35, 88))
        self.toggle_location = 324
        self.clicked = False

    def draw_screen(self):
        # draw text
        self.game_paused.draw(self.game.screen)
        self.rest_text.draw(self.game.screen)
        self.time.draw(self.game.screen)
        self.time.text = 'Time: {}:00'.format(self.game.time % 24)

        # draw buttons
        # RESUME button
        self.rest_button.draw(self.game.screen)
        self.rest_button_text.draw(self.game.screen)
        # BACK button
        self.back_button.draw(self.game.screen)
        self.back_button_text.draw(self.game.screen)

        # draw usernames
        self.u1_text.draw(self.game.screen)
        self.u2_text.draw(self.game.screen)
        self.u3_text.draw(self.game.screen)
        self.u4_text.draw(self.game.screen)
        # draw health bars
        self.u1_health.draw(self.game.screen)
        self.u2_health.draw(self.game.screen)
        self.u3_health.draw(self.game.screen)
        self.u4_health.draw(self.game.screen)

        # draw REST bar
        self.game.screen.blit(self.restbar, (195, 395))
        self.hours_text.draw(self.game.screen)
        # draw REST toggle
        self.game.screen.blit(self.restbar_toggle, (self.toggle_location, 404))

    def change_hour(self, mx, my):
        if 404 < my < 494:
            # 1 hour
            if 316 < mx <= 368.73:
                self.hours_text.text = "1 Hour"
                self.hours = 1
                self.toggle_location = 324
            # 2 hours
            elif 368.73 < mx <= 421.46:
                self.hours_text.text = "2 Hours"
                self.hours = 2
                self.toggle_location = 377
            # 3 hours
            elif 421.46 < mx <= 474.19:
                self.hours_text.text = "3 Hours"
                self.hours = 3
                self.toggle_location = 429.46
            # 4 hours
            elif 474.19 < mx <= 526.92:
                self.hours_text.text = "4 Hours"
                self.hours = 4
                self.toggle_location = 482.19
            # 5 hours
            elif 526.92 < mx <= 579.65:
                self.hours_text.text = "5 Hours"
                self.hours = 5
                self.toggle_location = 535
            # 6 hours
            elif 579.65 < mx <= 632.38:
                self.hours_text.text = "6 Hours"
                self.hours = 6
                self.toggle_location = 588
            # 7 hours
            elif 632.38 < mx <= 685.11:
                self.hours_text.text = "7 Hours"
                self.hours = 7
                self.toggle_location = 640.38
            # 8 hours
            elif 685.11 < mx <= 737.84:
                self.hours_text.text = "8 Hours"
                self.hours = 8
                self.toggle_location = 693.11
            # 9 hours
            elif 737.84 < mx <= 790.57:
                self.hours_text.text = "9 Hours"
                self.hours = 9
                self.toggle_location = 746
            # 10 hours
            elif 790.57 < mx <= 843.3:
                self.hours_text.text = "10 Hours"
                self.hours = 10
                self.toggle_location = 799
            # 11 hours
            elif 843.3 < mx <= 896.03:
                self.hours_text.text = "11 Hours"
                self.hours = 11
                self.toggle_location = 851.3
            # 12 hours
            elif 896.03 < mx <= 948.76:
                self.hours_text.text = "12 Hours"
                self.hours = 12
                self.toggle_location = 904

    def catch_actions(self, event, mx, my):
        # catch BACK button click
        self.back_button.change_menu(event, mx, my, "pitstop")

        # catch REST button click
        self.rest_button.rest(event, mx, my, self.hours)

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"

        # CATCH hours change ------------------------------------------#
        hovers = (316 < mx < 948.76) and (404 < my < 494)

        # clicked within bar
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and hovers:
            self.clicked = True
            self.change_hour(mx, my)

        # while still clicked, dynamically move bar
        if event.type == MOUSEMOTION and self.clicked and hovers:
            self.change_hour(mx, my)

        # let go of mouse
        if event.type == MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
