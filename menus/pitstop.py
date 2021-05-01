import pygame
from text import *
from button import *
from healthbar import *

class PitStop:
    def __init__(self, game):
        self.game = game

        # instantiate campfire image
        self.campfire = pygame.image.load('assets/campfire.png')
        self.campfire = pygame.transform.scale(self.campfire, (475, 257))

        x_offset = 100
        y_offset = 50
        # instantiate REST button
        self.rest_button = Button(x_offset, y_offset+80, 200, 70, LIGHT_GRAY, False, self.game)
        self.rest_button_text = Text('Rest', x_offset+100, y_offset+115, 30, BLACK)
        # instantiate MEDKIT button
        self.medkit_button = Button(x_offset, y_offset + 180, 200, 70, LIGHT_GRAY, False, self.game)
        self.medkit_button_text = Text('Medkit', x_offset + 100, y_offset + 217, 30, BLACK)
        # instantiate STRANGER button
        self.stranger_button = Button(x_offset, y_offset+280, 200, 70, LIGHT_GRAY, False, self.game)
        self.stranger_button_text = Text('Strangers', x_offset+100, y_offset+320, 27, BLACK)
        # instantiate JOBS button
        self.jobs_button = Button(x_offset, y_offset+380, 200, 70, LIGHT_GRAY, False, self.game)
        self.jobs_button_text = Text('Jobs', x_offset+100, y_offset+420, 30, BLACK)
        # instantiate MEDKIT ui
        self.medkit_text = Text('Medkit: {}'.format(self.game.medkits), 500, 50, 30, WHITE)

        x_offset2 = 0
        y_offset2 = 640
        # instantiate PARTY button
        self.party_button = Button(x_offset2+70, y_offset2, 200, 80, LIGHT_GRAY, False, self.game)
        self.party_button_text = Text('Party', x_offset2+170, y_offset2+43, 30, BLACK)
        # instantiate SUPPLIES button
        self.supplies_button = Button(x_offset2+300, y_offset2, 200, 80, LIGHT_GRAY, False, self.game)
        self.supplies_button_text = Text('Supplies', x_offset2+400, y_offset2+43, 30, BLACK)
        # instantiate BUY button
        self.buy_button = Button(x_offset2+530, y_offset2, 200, 80, LIGHT_GRAY, False, self.game)
        self.buy_button_text = Text('Shop', x_offset2+630, y_offset2+43, 30, BLACK)
        # instantiate BACK button
        self.back_button = Button(x_offset2+950, y_offset2, 200, 80, LIGHT_GRAY, False, self.game)
        self.back_button_text = Text('Back', x_offset2+1050, y_offset2+43, 30, BLACK)

        x_offset3 = 260
        y_offset3 = 85
        # instantiate GET MONEY text
        self.getmoney_text = Text('Get Money', x_offset3+100, y_offset3+130, 35, WHITE)
        # instantiate BLACKJACK button
        self.blackjack_button = Button(x_offset3, y_offset3+180, 200, 70, LIGHT_GRAY, False, self.game)
        self.blackjack_button_text = Text('Blackjack', x_offset3+103, y_offset3+217, 23, BLACK)
        # instantiate SLOT MACHINE button
        self.slotmachine_button = Button(x_offset3, y_offset3+280, 200, 70, LIGHT_GRAY, False, self.game)
        self.slotmachine_button_text = Text('Slot Machine', x_offset3+100, y_offset3+320, 22, BLACK)

        stat_x = 800
        stat_y = 300
        self.supply_count = Text('Supply Count', stat_x+90, stat_y-60, 35, WHITE)
        self.fuel_text = Text('Fuel: {}'.format(self.game.fuel), stat_x+89, stat_y, 27, WHITE)
        self.food_text = Text('Food: {}'.format(self.game.food), stat_x+100, stat_y+40, 27, WHITE)
        self.money_text = Text('Money: {}'.format(self.game.money), stat_x+104, stat_y+80, 27, WHITE)

        # usernames/healthbars
        user_x = 800
        user_y = 30
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

        buy_x = 640
        buy_y = 300
        # instantiate SUPPLIES texts
        self.suppliesShop_text = Text('Supplies Shop', self.game.width / 2, 70, 50, WHITE)
        self.buyFood_text = Text('Food: 100/$200', buy_x - 340, buy_y, 23, WHITE)
        self.buyFuel_text = Text('Fuel: 1/$100', buy_x, buy_y, 23, WHITE)
        self.buyMedkits_text = Text('Medkits: 1/$50', buy_x + 350, buy_y, 23, WHITE)
        # instantiate SUPPLIES buttons
        self.buyFood_button = Button(buy_x - 435, buy_y + 50, 200, 70, LIGHT_GRAY, False, self.game)
        self.buyFood_button_text = Text('Purchase', buy_x - 335, buy_y + 87, 27, BLACK)
        self.buyFuel_button = Button(buy_x - 100, buy_y + 50, 200, 70, LIGHT_GRAY, False, self.game)
        self.buyFuel_button_text = Text('Purchase', buy_x - 0, buy_y + 87, 27, BLACK)
        self.buyMedkits_button = Button(buy_x + 248, buy_y + 50, 200, 70, LIGHT_GRAY, False, self.game)
        self.buyMedkits_button_text = Text('Purchase', buy_x + 348, buy_y + 87, 27, BLACK)

    def draw_screen(self):
        # draw PARTY button
        self.party_button.draw(self.game.screen)
        self.party_button_text.draw(self.game.screen)
        # draw SUPPLIES button
        self.supplies_button.draw(self.game.screen)
        self.supplies_button_text.draw(self.game.screen)
        # draw BUY button
        self.buy_button.draw(self.game.screen)
        self.buy_button_text.draw(self.game.screen)
        # draw BACK button
        self.back_button.draw(self.game.screen)
        self.back_button_text.draw(self.game.screen)

        if self.game.pitstop_menu == "party":
            # shade buttons appropriately
            self.party_button.color = DARK_GRAY
            self.supplies_button.color = LIGHT_GRAY
            self.buy_button.color = LIGHT_GRAY

            # draw campfire
            self.game.screen.blit(self.campfire, (700, 275))
            # draw medkit text
            self.medkit_text.text = 'Medkit: {}'.format(self.game.medkits)
            self.medkit_text.draw(self.game.screen)

            # draw REST button
            self.rest_button.draw(self.game.screen)
            self.rest_button_text.draw(self.game.screen)
            # draw MEDKIT button
            self.medkit_button.draw(self.game.screen)
            self.medkit_button_text.draw(self.game.screen)
            # draw STRANGER button
            self.stranger_button.draw(self.game.screen)
            self.stranger_button_text.draw(self.game.screen)
            # draw JOBS button
            self.jobs_button.draw(self.game.screen)
            self.jobs_button_text.draw(self.game.screen)

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

        elif self.game.pitstop_menu == "supplies":
            # shade buttons appropriately
            self.party_button.color = LIGHT_GRAY
            self.supplies_button.color = DARK_GRAY
            self.buy_button.color = LIGHT_GRAY

            # GET MONEY text
            self.getmoney_text.draw(self.game.screen)

            # draw BLACKJACK button
            self.blackjack_button.draw(self.game.screen)
            self.blackjack_button_text.draw(self.game.screen)
            # draw SLOT MACHINE button
            self.slotmachine_button.draw(self.game.screen)
            self.slotmachine_button_text.draw(self.game.screen)

            # draw "Supply Count" Text
            self.supply_count.draw(self.game.screen)
            # draw supplies count
            self.fuel_text.text = 'Fuel: {}'.format(self.game.fuel)    # fuel
            self.fuel_text.draw(self.game.screen)
            self.food_text.text = 'Food: {}'.format(self.game.food)    # food
            self.food_text.draw(self.game.screen)
            self.money_text.text = 'Money: {}'.format(self.game.money)        # money
            self.money_text.draw(self.game.screen)

        elif self.game.pitstop_menu == "buy":
            # shade buttons appropriately
            self.party_button.color = LIGHT_GRAY
            self.supplies_button.color = LIGHT_GRAY
            self.buy_button.color = DARK_GRAY

            # draw "Supplies Shop" Text
            self.suppliesShop_text.draw(self.game.screen)

            # draw Supplies Text
            self.buyFood_text.draw(self.game.screen)
            self.buyFuel_text.draw(self.game.screen)
            self.buyMedkits_text.draw(self.game.screen)

            # draw Supplies Buttons
            self.buyFood_button.draw(self.game.screen)
            self.buyFood_button_text.draw(self.game.screen)
            self.buyFuel_button.draw(self.game.screen)
            self.buyFuel_button_text.draw(self.game.screen)
            self.buyMedkits_button.draw(self.game.screen)
            self.buyMedkits_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        if self.game.pitstop_menu == "party":
            # catch REST button click
            self.rest_button.change_menu(event, mx, my, "rest")
            # catch MEDKIT button click
            self.medkit_button.medkit(event, mx, my, self.medkit_text)
            # catch STRANGER button click
            self.stranger_button.change_menu(event, mx, my, "stranger")
            # catch JOBS button click
            self.jobs_button.change_menu(event, mx, my, "jobs")

        elif self.game.pitstop_menu == "supplies":
            # catch SLOT MACHINE play
            self.slotmachine_button.change_menu(event, mx, my, "slotmachine")
            # catch BLACKJACK play
            self.blackjack_button.change_menu(event, mx, my, "blackjack")

        elif self.game.pitstop_menu == "buy":
            # catch PURCHASES
            self.buyFuel_button.purchase(event, mx, my, "fuel")
            self.buyFood_button.purchase(event, mx, my, "food")
            self.buyMedkits_button.purchase(event, mx, my, "medkits")

        # catch UI changes
        self.party_button.change_ui(event, mx, my, "pitstop", "party")
        self.supplies_button.change_ui(event, mx, my, "pitstop", "supplies")
        self.buy_button.change_ui(event, mx, my, "pitstop", "buy")

        # catch BACK button click
        self.back_button.change_menu(event, mx, my, "play")

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"