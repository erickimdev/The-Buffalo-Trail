import pygame
from pygame.locals import *
from colors import *
import random

#Initialize Game
pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont('arial', 35)
fontfortitle = pygame.font.SysFont('arial', 55)

gametxt = fontfortitle.render('BlackJack', 1, WHITE)
dealerTxt = font.render('Dealer', 1, WHITE)
playerTxt = font.render('Player', 1, WHITE)

hitTxt = font.render('Hit', 1, WHITE)
standTxt = font.render('Stand', 1, WHITE)
restartTxt = font.render('Restart', 1, WHITE)
gameoverTxt = font.render('GAME OVER', 1, WHITE)

glitchTxt = font.render('GAME CHANGING CARD', 1, WHITE)

background = pygame.Surface(screen.get_size())
background.fill(BLACK)

hitButton = pygame.draw.rect(background, GRAY, (900, 400, 80, 35))
standButton = pygame.draw.rect(background, GRAY, (990, 400, 80, 35))

#initializing cards
diamondA = pygame.transform.scale(pygame.image.load('assets/cards/ace_of_diamonds.png'), (100, 120))
clubA = pygame.transform.scale(pygame.image.load('assets/cards/ace_of_clubs.png'), (100, 120))
heartA = pygame.transform.scale(pygame.image.load('assets/cards/ace_of_hearts.png'), (100, 120))
spadeA = pygame.transform.scale(pygame.image.load('assets/cards/ace_of_spades.png'), (100, 120))
diamond2 = pygame.transform.scale(pygame.image.load('assets/cards/2_of_diamonds.png'), (100, 120))
club2 = pygame.transform.scale(pygame.image.load('assets/cards/2_of_clubs.png'), (100, 120))
heart2 = pygame.transform.scale(pygame.image.load('assets/cards/2_of_hearts.png'), (100, 120))
spade2 = pygame.transform.scale(pygame.image.load('assets/cards/2_of_spades.png'), (100, 120))
diamond3 = pygame.transform.scale(pygame.image.load('assets/cards/3_of_diamonds.png'), (100, 120))
club3 = pygame.transform.scale(pygame.image.load('assets/cards/3_of_clubs.png'), (100, 120))
heart3 = pygame.transform.scale(pygame.image.load('assets/cards/3_of_hearts.png'), (100, 120))
spade3 = pygame.transform.scale(pygame.image.load('assets/cards/3_of_spades.png'), (100, 120))
diamond4 = pygame.transform.scale(pygame.image.load('assets/cards/4_of_diamonds.png'), (100, 120))
club4 = pygame.transform.scale(pygame.image.load('assets/cards/4_of_clubs.png'), (100, 120))
heart4 = pygame.transform.scale(pygame.image.load('assets/cards/4_of_hearts.png'), (100, 120))
spade4 = pygame.transform.scale(pygame.image.load('assets/cards/4_of_spades.png'), (100, 120))
diamond5 = pygame.transform.scale(pygame.image.load('assets/cards/5_of_diamonds.png'), (100, 120))
club5 = pygame.transform.scale(pygame.image.load('assets/cards/5_of_clubs.png'), (100, 120))
heart5 = pygame.transform.scale(pygame.image.load('assets/cards/5_of_hearts.png'), (100, 120))
spade5 = pygame.transform.scale(pygame.image.load('assets/cards/5_of_spades.png'), (100, 120))
diamond6 = pygame.transform.scale(pygame.image.load('assets/cards/6_of_diamonds.png'), (100, 120))
club6 = pygame.transform.scale(pygame.image.load('assets/cards/6_of_clubs.png'), (100, 120))
heart6 = pygame.transform.scale(pygame.image.load('assets/cards/6_of_hearts.png'), (100, 120))
spade6 = pygame.transform.scale(pygame.image.load('assets/cards/6_of_spades.png'), (100, 120))
diamond7 = pygame.transform.scale(pygame.image.load('assets/cards/7_of_diamonds.png'), (100, 120))
club7 = pygame.transform.scale(pygame.image.load('assets/cards/7_of_clubs.png'), (100, 120))
heart7 = pygame.transform.scale(pygame.image.load('assets/cards/7_of_hearts.png'), (100, 120))
spade7 = pygame.transform.scale(pygame.image.load('assets/cards/7_of_spades.png'), (100, 120))
diamond8 = pygame.transform.scale(pygame.image.load('assets/cards/8_of_diamonds.png'), (100, 120))
club8 = pygame.transform.scale(pygame.image.load('assets/cards/8_of_clubs.png'), (100, 120))
heart8 = pygame.transform.scale(pygame.image.load('assets/cards/8_of_hearts.png'), (100, 120))
spade8 = pygame.transform.scale(pygame.image.load('assets/cards/8_of_spades.png'), (100, 120))
diamond9 = pygame.transform.scale(pygame.image.load('assets/cards/9_of_diamonds.png'), (100, 120))
club9 = pygame.transform.scale(pygame.image.load('assets/cards/9_of_clubs.png'), (100, 120))
heart9 = pygame.transform.scale(pygame.image.load('assets/cards/9_of_hearts.png'), (100, 120))
spade9 = pygame.transform.scale(pygame.image.load('assets/cards/9_of_spades.png'), (100, 120))
diamond10 = pygame.transform.scale(pygame.image.load('assets/cards/10_of_diamonds.png'), (100, 120))
club10 = pygame.transform.scale(pygame.image.load('assets/cards/10_of_clubs.png'), (100, 120))
heart10 = pygame.transform.scale(pygame.image.load('assets/cards/10_of_hearts.png'), (100, 120))
spade10 = pygame.transform.scale(pygame.image.load('assets/cards/10_of_spades.png'), (100, 120))
diamondJ = pygame.transform.scale(pygame.image.load('assets/cards/jack_of_diamonds.png'), (100, 120))
clubJ = pygame.transform.scale(pygame.image.load('assets/cards/jack_of_clubs.png'), (100, 120))
heartJ = pygame.transform.scale(pygame.image.load('assets/cards/jack_of_hearts.png'), (100, 120))
spadeJ = pygame.transform.scale(pygame.image.load('assets/cards/jack_of_spades.png'), (100, 120))
diamondQ = pygame.transform.scale(pygame.image.load('assets/cards/queen_of_diamonds.png'), (100, 120))
clubQ = pygame.transform.scale(pygame.image.load('assets/cards/queen_of_clubs.png'), (100, 120))
heartQ = pygame.transform.scale(pygame.image.load('assets/cards/queen_of_hearts.png'), (100, 120))
spadeQ = pygame.transform.scale(pygame.image.load('assets/cards/queen_of_spades.png'), (100, 120))
diamondK = pygame.transform.scale(pygame.image.load('assets/cards/king_of_diamonds.png'), (100, 120))
clubK = pygame.transform.scale(pygame.image.load('assets/cards/king_of_clubs.png'), (100, 120))
heartK = pygame.transform.scale(pygame.image.load('assets/cards/king_of_hearts.png'), (100, 120))
spadeK = pygame.transform.scale(pygame.image.load('assets/cards/king_of_spades.png'), (100, 120))

suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

card_dict = {'Heart2': heart2,'Heart3': heart3,'Heart4': heart4,'Heart5': heart5,'Heart6': heart6,'Heart7': heart7,'Heart8': heart8,'Heart9': heart9,'Heart10': heart10,'HeartK': heartK,'HeartQ': heartQ,'HeartJ': heartJ,'HeartA': heartA
    ,'Diamond2': diamond2,'Diamond3': diamond3,'Diamond4': diamond4,'Diamond5': diamond5,'Diamond6': diamond6,'Diamond7': diamond7,'Diamond8': diamond8,'Diamond9': diamond9,'Diamond10': diamond10,'DiamondK': diamondK,'DiamondQ': diamondQ,'DiamondJ': diamondJ,'DiamondA': diamondA
    ,'Spade2': spade2,'Spade3': spade3,'Spade4': spade4,'Spade5': spade5,'Spade6': spade6,'Spade7': spade7,'Spade8': spade8,'Spade9': spade9,'Spade10': spade10,'SpadeK': spadeK,'SpadeQ': spadeQ,'SpadeJ': spadeJ,'SpadeA': spadeA
    ,'Club2':club2,'Club3':club3,'Club4':club4,'Club5':club5,'Club6':club6,'Club7':club7,'Club8':club8,'Club9':club9,'Club10':club10,'ClubK':clubK,'ClubQ':clubQ,'ClubJ':clubJ,'ClubA':clubA}
card_value_dict = {'Heart2': 2,'Heart3': 3,'Heart4': 4,'Heart5': 5,'Heart6': 6,'Heart7': 7,'Heart8': 8,'Heart9': 9,'Heart10': 10,'HeartK': 10,'HeartQ': 10,'HeartJ': 10,'HeartA': 11
    ,'Diamond2': 2,'Diamond3': 3,'Diamond4': 4,'Diamond5': 5,'Diamond6': 6,'Diamond7': 7,'Diamond8': 8,'Diamond9': 9,'Diamond10': 10,'DiamondK': 10,'DiamondQ': 10,'DiamondJ': 10,'DiamondA': 11
    ,'Spade2': 2,'Spade3': 3,'Spade4': 4,'Spade5': 5,'Spade6':6,'Spade7': 7,'Spade8': 8,'Spade9': 9,'Spade10': 10,'SpadeK': 10,'SpadeQ': 10,'SpadeJ': 10,'SpadeA': 11
    ,'Club2': 2,'Club3':3,'Club4':4,'Club5':5,'Club6':6,'Club7':7,'Club8':8,'Club9':9,'Club10':10,'ClubK':10,'ClubQ':10,'ClubJ':10,'ClubA':11}

class BlackJack:
    def __init__(self, game):
        self.game = game

        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(suit+rank)
        self.total = self.game.money
        self.duplicatecards = self.deck.copy() #copy.copy(cards)
        self.stand = False
        self.userCard = []
        self.dealerCard = []
        self.winNum = 0

        #checks if game is over
        self.gameover = False

        #get sums and aces in the initial drawn cards
        self.userSum, self.userA, self.dealSum, self.dealA = self.initGame(self.duplicatecards, self.userCard, self.dealerCard)

    # generates two cards for dealer and user, one at a time for each.Returns if card is Ace and the total amount of the cards per person.
    def initGame(self, cList, uList, dList):
        userAces = 0
        dealAces = 0

        random.shuffle(self.deck)

        Usercard1 = self.deck.pop()
        cList.remove(Usercard1)
        uList.append(Usercard1)
        if card_value_dict[Usercard1] == 11:
            userAces += 1

        Usercard2 = self.deck.pop()
        cList.remove(Usercard2)
        uList.append(Usercard2)
        if card_value_dict[Usercard2] == 11:
            userAces += 1

        random.shuffle(self.deck)

        DealerCard1 = self.deck.pop()
        cList.remove(DealerCard1)
        dList.append(DealerCard1)
        if card_value_dict[DealerCard1] == 11:
            dealAces += 1

        DealerCard2 = self.deck.pop()
        cList.remove(DealerCard2)
        dList.append(DealerCard2)
        if card_value_dict[DealerCard2] == 11:
            dealAces += 1

        return card_value_dict[Usercard1] + card_value_dict[Usercard2], userAces, card_value_dict[DealerCard1] + card_value_dict[DealerCard2], dealAces

    def draw_screen(self):
        # background needs to be redisplayed because it gets updated
        winTxt = font.render('Wins: %i' % self.winNum, 1, WHITE)
        cashTxt = font.render('Balance Cash: %i' % self.game.money, 1, WHITE)

        # checks for mouse clicks on buttons
        screen.blit(background, (0, 0))

        screen.blit(gametxt, (600, 0))
        screen.blit(dealerTxt, (660, 100))
        screen.blit(playerTxt, (660, 400))

        screen.blit(hitTxt, (910, 400))
        screen.blit(standTxt, (990, 400))
        screen.blit(winTxt, (220, 575))
        screen.blit(cashTxt, (900, 20))

        screen.blit(glitchTxt, (20, 130))

        # displays dealer's cards
        x1 = 550
        for card in self.dealerCard:
            screen.blit(card_dict[card], (x1, 200))
            x1 += 150

        # displays player's cards
        x2 = 550
        for card in self.userCard:
            screen.blit(card_dict[card], (x2, 500))
            x2 += 150

        # when game is over, draws restart button and text, and shows the dealer's second card
        if self.gameover or self.stand:
            screen.blit(gameoverTxt, (240, 380))
            self.restartButton = pygame.draw.rect(background, GRAY, (270, 325, 100, 35))
            screen.blit(restartTxt, (275, 323))
            screen.blit(card_dict[self.dealerCard[1]], (120, 10))

    def catch_actions(self, event, mx, my):
        # press esc key to go back to PITSOP
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.menu_state = "pitstop"

        if (self.userSum >= 21 and self.userA == 0):
            self.gameover = True

        if len(self.userCard) == 2 and self.userSum == 21:
            self.gameover = True
        elif len(self.dealerCard) == 2 and self.dealSum == 21:
            self.gameover = True

        if event.type == pygame.MOUSEBUTTONDOWN and not (self.gameover or self.stand) and hitButton.collidepoint(pygame.mouse.get_pos()):
            # gives player a card if they don't break blackjack rules
            # player
            card = self.deck.pop()
            self.duplicatecards.remove(card)
            self.userCard.append(card)
            if card_value_dict[card] == 11:
                self.userA += 1

            # dealer
            self.userSum += card_value_dict[card]
            while self.userSum > 21 and self.userA > 0:
                self.userA -= 1
                self.userSum -= 10

        elif event.type == pygame.MOUSEBUTTONDOWN and not self.gameover and standButton.collidepoint(pygame.mouse.get_pos()):
            # when player stands, the dealer plays
            stand = True
            while self.dealSum <= self.userSum and self.dealSum < 20:
                # for players
                card = self.deck.pop()
                self.duplicatecards.remove(card)
                self.dealerCard.append(card)
                if card_value_dict[card] == 11:
                    self.dealA += 1

                # for dealer
                self.dealSum += card_value_dict[card]
                while self.dealSum > 21 and self.dealA > 0:
                    self.dealA -= 1
                    self.dealSum -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and (self.gameover or self.stand) and self.restartButton.collidepoint(pygame.mouse.get_pos()):
            # restarts the game, updating scores
            if self.userSum == self.dealSum:
                pass
            elif self.userSum <= 21:
                self.winNum += 1
                self.total += 25
                self.game.money += 25
            elif self.userSum <= 21 and self.dealSum < self.userSum or self.dealSum > 21:
                self.winNum += 1
                self.total += 25
                self.game.money += 25
            else:
                self.total -= 25
                self.game.money -= 25

            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(suit+rank)

            self.gameover = False
            self.stand = False
            self.userCard = []
            self.dealerCard = []
            self.duplicatecards = self.deck.copy()
            self.userSum, self.userA, self.dealSum, self.dealA = self.initGame(self.duplicatecards, self.userCard, self.dealerCard)

            self.restartButton = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))