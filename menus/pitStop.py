import pygame
from text import *
from button import *

class PitStop:
    def __init__(self, game):
        self.game = game

        # instantiate Pit stop header
        self.pit_stop = Text('Pit Stop', self.game.width/2, 130, 60, WHITE)

        # instantiate Map button
        self.map_button = Button(360, 210, 200, 70, LIGHT_GRAY, False, self.game)
        self.map_button_text = Text('Map',460 , 250, 30, BLACK)
        # instantiate Heal button
        self.heal_button = Button(700, 210, 200, 70, LIGHT_GRAY, False, self.game)
        self.heal_button_text = Text('Heal', 800, 250, 30, BLACK)
        # instantiate Talk to stranger button
        self.talk_to_stranger_button = Button(360, 310, 200, 70, LIGHT_GRAY, False, self.game)
        self.talk_to_stranger1_button_text = Text('Talk to', 460,340, 20, BLACK)
        self.talk_to_stranger2_button_text = Text('Stranger', 460,360, 20, BLACK)
        # instantiate Shop button
        self.shop_button = Button(700, 310, 200, 70, LIGHT_GRAY, False, self.game)
        self.shop_button_text = Text('Shop', 800, 350, 30, BLACK)
        # instantiate Scavenge button
        self.scavenge_button = Button(360, 410, 200, 70, LIGHT_GRAY, False, self.game)
        self.scavenge_button_text = Text('Scavenge', 460, 450, 30, BLACK)
        # instantiate Jobs button
        self.job_button = Button(700, 410, 200, 70, LIGHT_GRAY, False, self.game)
        self.job_button_text = Text('Jobs', 800, 450, 30, BLACK)
        # instantiate Resume button
        self.resume_button = Button(530, 610, 200, 70, LIGHT_GRAY, False, self.game)
        self.resume_button_text = Text('Resume', 630, 650, 30, BLACK)

    def draw_screen(self):
        # draw Pit Stop header
        self.pit_stop.draw(self.game.screen)

        # draw buttons
        # MAP button
        self.map_button.draw(self.game.screen)
        self.map_button_text.draw(self.game.screen)
        # HEAL button
        self.heal_button.draw(self.game.screen)
        self.heal_button_text.draw(self.game.screen)
        # Talk to Stranger button
        self.talk_to_stranger_button.draw(self.game.screen)
        self.talk_to_stranger1_button_text.draw(self.game.screen)
        self.talk_to_stranger2_button_text.draw(self.game.screen)
        # SHOP button
        self.shop_button.draw(self.game.screen)
        self.shop_button_text.draw(self.game.screen)
        # SCAVENGE button
        self.scavenge_button.draw(self.game.screen)
        self.scavenge_button_text.draw(self.game.screen)
        # JOB button
        self.job_button.draw(self.game.screen)
        self.job_button_text.draw(self.game.screen)
        # resume button
        self.resume_button.draw(self.game.screen)
        self.resume_button_text.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        
        # catch SAVE button click
        self.talk_to_stranger_button.change_menu(event, mx, my, "talkToStranger")
        # catch RESUME button click
        self.resume_button.change_menu(event, mx, my, "play")

        # press esc key to UNPAUSE
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.game.menu_state = "play"