import pygame
from pygame.locals import *
from button import *
from text import *
from healthbar import *

class Play:
    def __init__(self, game):
        self.game = game

        # instantiate CLICK ANYWHERE header
        self.click_anywhere = Text('Click Anywhere to Travel', self.game.width / 2, 50, 20, WHITE)

        # instantiate car image
        self.car = pygame.image.load('assets/car.png')
        self.car = pygame.transform.scale(self.car, (250, 140))

        # instantiate PAUSE GAME button
        self.pause_button = Button(10, 10, 35, 35, (210,210,210), False, self.game)
        self.pause_button_text = Text('II', 29, 29, 27, BLACK)

        # coord offsets
        button_x = 1055
        button_y = 255
        # HEALTH
            # button
        self.health_button = Button(button_x, button_y+210, 200, 70, LIGHT_GRAY, False, self.game)
        self.health_button_text = Text('Health', button_x+100, button_y+250, 30, BLACK)
            # usernames
        user_x = 400
        user_y = 510
        self.car_text = Text('BMW X6', user_x, user_y, 27, WHITE)
        self.u1_text = Text('User 1', user_x, user_y+40, 27, WHITE)
        self.u2_text = Text('User 2', user_x, user_y+80, 27, WHITE)
        self.u3_text = Text('User 3', user_x, user_y+120, 27, WHITE)
        self.u4_text = Text('User 4', user_x, user_y+160, 27, WHITE)
            # health bars
        self.car_health = Healthbar(self.game, user_x+105, user_y-17, "car")
        self.u1_health = Healthbar(self.game, user_x+105, user_y+23, "u1")
        self.u2_health = Healthbar(self.game, user_x+105, user_y+63, "u2")
        self.u3_health = Healthbar(self.game, user_x+105, user_y+103, "u3")
        self.u4_health = Healthbar(self.game, user_x+105, user_y+143, "u4")

        # STATS
            # button
        self.stats_button = Button(button_x, button_y+295, 200, 70, LIGHT_GRAY, False, self.game)
        self.stats_button_text = Text('Stats', button_x+100, button_y+335, 30, BLACK)
            # stat texts
        stat_x = 400
        stat_y = 527
        self.fuel_text = Text('Fuel: {} gallons'.format(self.game.fuel), stat_x+153, stat_y, 27, WHITE)
        self.food_text = Text('Food: {} oz'.format(self.game.food), stat_x+117, stat_y+40, 27, WHITE)
        self.miles_left_text = Text('Distance to Buffalo: {} miles'.format(self.game.miles_left), stat_x, stat_y+80, 27, WHITE)
        self.traveled_text = Text('Miles Traveled: {} miles'.format(self.game.traveled), stat_x+37, stat_y+120, 27, WHITE)

        # PITSTOP button
        self.pitstop_button = Button(button_x, button_y+380, 200, 70, LIGHT_GRAY, False, self.game)
        self.pitstop_button_text = Text('Pitstop', button_x+100, button_y+420, 30, BLACK)

    def draw_screen(self):
        # draw instructions
        self.click_anywhere.draw(self.game.screen)
        # draw light blue backdrop
        pygame.draw.rect(self.game.screen, (112, 128, 144), (0, 450, self.game.width, 500), 0)
        # draw road
        pygame.draw.rect(self.game.screen, WHITE, (0, 310, self.game.width, 7), 0)
        pygame.draw.rect(self.game.screen, WHITE, (0, 380, self.game.width, 7), 0)
        ct = 0
        for i in range(20):
            pygame.draw.rect(self.game.screen, WHITE, (ct*100, 345, 50, 7), 0)
            ct += 1
        # draw car
        self.game.screen.blit(self.car, (930, 233))

        # draw PAUSE button
        self.pause_button.draw(self.game.screen)
        self.pause_button_text.draw(self.game.screen)
        # draw HEALTH button
        self.health_button.draw(self.game.screen)
        self.health_button_text.draw(self.game.screen)
        # draw STATS button
        self.stats_button.draw(self.game.screen)
        self.stats_button_text.draw(self.game.screen)
        # draw STOP button
        self.pitstop_button.draw(self.game.screen)
        self.pitstop_button_text.draw(self.game.screen)

        # HEALTH selected
        if self.game.button_selected == 'health':
            # shade buttons appropriately
            self.health_button.color = DARK_GRAY
            self.stats_button.color = LIGHT_GRAY
            self.pitstop_button.color = LIGHT_GRAY

            # draw usernames
            self.car_text.draw(self.game.screen)
            self.u1_text.draw(self.game.screen)
            self.u2_text.draw(self.game.screen)
            self.u3_text.draw(self.game.screen)
            self.u4_text.draw(self.game.screen)

            # draw health bars
            self.car_health.draw(self.game.screen)
            self.u1_health.draw(self.game.screen)
            self.u2_health.draw(self.game.screen)
            self.u3_health.draw(self.game.screen)
            self.u4_health.draw(self.game.screen)

    # STATS selected
        elif self.game.button_selected == 'stats':
            # shade buttons appropriately
            self.health_button.color = LIGHT_GRAY
            self.stats_button.color = DARK_GRAY
            self.pitstop_button.color = LIGHT_GRAY

            # update stats
            self.fuel_text.text = 'Fuel: {} gallons'.format(self.game.fuel)
            self.food_text.text = 'Food: {} oz'.format(self.game.food)
            self.miles_left_text.text = 'Distance to Buffalo: {} miles'.format(self.game.miles_left)
            self.traveled_text.text = 'Miles Traveled: {} miles'.format(self.game.traveled)

            # draw stats
            self.fuel_text.draw(self.game.screen)
            self.food_text.draw(self.game.screen)
            self.miles_left_text.draw(self.game.screen)
            self.traveled_text.draw(self.game.screen)

        # pitstop selected
        elif self.game.button_selected == 'pitstop':
            # shade buttons appropriately
            self.health_button.color = LIGHT_GRAY
            self.stats_button.color = LIGHT_GRAY
            self.pitstop_button.color = DARK_GRAY

    def catch_actions(self, event, mx, my):
        # if travelling (left click)
        x = 0
        y = 60
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if x < mx < x + self.game.width:
                if y < my < y + 400:
                    # update state
                    self.game.fuel -= 1
                    self.game.food -= (self.game.alive * 10)
                    self.game.miles_left -= 10
                    self.game.traveled += 10

        # catch PAUSE button clicks
        self.pause_button.change_menu(event, mx, my, "pause")

        # catch UI changes
        self.health_button.change_ui(event, mx, my, "gameplay", "health")
        self.stats_button.change_ui(event, mx, my, "gameplay", "stats")
        self.pitstop_button.change_ui(event, mx , my, "gameplay", "pitstop")

        # press esc key to PAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "pause"