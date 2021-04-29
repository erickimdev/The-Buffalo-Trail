import pygame
from pygame.locals import *
from colors import *
from text import *
from button import *

class Blackjack:
    def __init__(self,game):
        self.game = game
        self.total = 1000 #change
        self.result_text = Text('PLAYER BUSTS!', 500, 800, 28, BLACK)

        #initializing cards

        self.diamondA = pygame.image.load('assets/cards/ace_of_diamonds.png')
        self.diamondA = pygame.transform.scale(diamondA, (120, 120)) 

        self.clubA = pygame.image.load('assets/cards/ace_of_clubs.png')
        self.clubA = pygame.transform.scale(clubA, (120, 120)) 

        self.heartA = pygame.image.load('assets/cards/ace_of_hearts.png')
        self.heartA = pygame.transform.scale(heartA, (120, 120)) 

        self.spadeA = pygame.image.load('assets/cards/ace_of_spades.png')
        self.spadeA = pygame.transform.scale(spadeA, (120, 120)) 

        self.diamond2 = pygame.image.load('assets/cards/2_of_diamonds.png')
        self.diamond2 = pygame.transform.scale(diamond2, (120, 120)) 

        self.club2 = pygame.image.load('assets/cards/2_of_clubs.png')
        self.club2 = pygame.transform.scale(club2, (120, 120)) 

        self.heart2 = pygame.image.load('assets/cards/2_of_hearts.png')
        self.heart2 = pygame.transform.scale(heart2, (120, 120)) 

        self.spade2 = pygame.image.load('assets/cards/2_of_spades.png')
        self.spade2 = pygame.transform.scale(spade2, (120, 120)) 

        self.diamond3 = pygame.image.load('assets/cards/3_of_diamonds.png')
        self.diamond3 = pygame.transform.scale(diamond3, (120, 120)) 

        self.club3 = pygame.image.load('assets/cards/3_of_clubs.png')
        self.club3 = pygame.transform.scale(club3, (120,120)) 

        self.heart3 = pygame.image.load('assets/cards/3_of_hearts.png')
        self.heart3 = pygame.transform.scale(heart3, (120, 120)) 

        self.spade3 = pygame.image.load('assets/cards/3_of_spades.png')
        self.spade3 = pygame.transform.scale(spade3, (120, 120)) 

        self.diamond4 = pygame.image.load('assets/cards/4_of_diamonds.png')
        self.diamond4 = pygame.transform.scale(diamond4, (120, 120)) 

        self.club4 = pygame.image.load('assets/cards/4_of_clubs.png')
        self.club4 = pygame.transform.scale(club4, (120, 120)) 

        self.heart4 = pygame.image.load('assets/cards/4_of_hearts.png')
        self.heart4 = pygame.transform.scale(heart4, (120, 120)) 

        self.spade4 = pygame.image.load('assets/cards/4_of_spades.png')
        self.spade4 = pygame.transform.scale(spade4, (120, 120)) 

        self.diamond5 = pygame.image.load('assets/cards/5_of_diamonds.png')
        self.diamond5 = pygame.transform.scale(diamond5, (120, 120)) 

        self.club5 = pygame.image.load('assets/cards/5_of_clubs.png')
        self.club5 = pygame.transform.scale(club5, (120, 120)) 

        self.heart5 = pygame.image.load('assets/cards/5_of_hearts.png')
        self.heart5 = pygame.transform.scale(heart5, (120, 120)) 

        self.spade5 = pygame.image.load('assets/cards/5_of_spades.png')
        self.spade5 = pygame.transform.scale(spade5, (120, 120)) 

        self.diamond6 = pygame.image.load('assets/cards/6_of_diamonds.png')
        self.diamond6 = pygame.transform.scale(diamond6, (120, 120)) 

        self.club6 = pygame.image.load('assets/cards/6_of_clubs.png')
        self.club6 = pygame.transform.scale(club6, (120, 120)) 

        self.heart6 = pygame.image.load('assets/cards/6_of_hearts.png')
        self.heart6 = pygame.transform.scale(heart6, (120, 120)) 

        self.spade6 = pygame.image.load('assets/cards/6_of_spades.png')
        self.spade6 = pygame.transform.scale(spade6, (120, 120)) 

        self.diamond7 = pygame.image.load('assets/cards/7_of_diamonds.png')
        self.diamond7 = pygame.transform.scale(diamond7, (120, 120)) 

        self.club7 = pygame.image.load('assets/cards/7_of_clubs.png')
        self.club7 = pygame.transform.scale(club7, (120, 120)) 

        self.heart7 = pygame.image.load('assets/cards/7_of_hearts.png')
        self.heart7 = pygame.transform.scale(heart7, (120, 120)) 

        self.spade7 = pygame.image.load('assets/cards/7_of_spades.png')
        self.spade7 = pygame.transform.scale(spade7, (120, 120)) 

        self.diamond8 = pygame.image.load('assets/cards/8_of_diamonds.png')
        self.diamond8 = pygame.transform.scale(diamond8, (120, 120)) 

        self.club8 = pygame.image.load('assets/cards/8_of_clubs.png')
        self.club8 = pygame.transform.scale(club8, (120, 120)) 

        self.heart8 = pygame.image.load('assets/cards/8_of_hearts.png')
        self.heart8 = pygame.transform.scale(heart8, (120, 120)) 

        self.spade8 = pygame.image.load('assets/cards/8_of_spades.png')
        self.spade8 = pygame.transform.scale(spade8, (120, 120)) 

        self.diamond9 = pygame.image.load('assets/cards/9_of_diamonds.png')
        self.diamond9 = pygame.transform.scale(diamond9, (120, 120)) 

        self.club9 = pygame.image.load('assets/cards/9_of_clubs.png')
        self.club9 = pygame.transform.scale(club9, (120, 120)) 

        self.heart9 = pygame.image.load('assets/cards/9_of_hearts.png')
        self.heart9 = pygame.transform.scale(heart9, (120, 120)) 

        self.spade9 = pygame.image.load('assets/cards/9_of_spades.png')
        self.spade9 = pygame.transform.scale(spade9, (120, 120)) 

        self.diamond10 = pygame.image.load('assets/cards/10_of_diamonds.png')
        self.diamond10 = pygame.transform.scale(diamond10, (120, 120)) 

        self.club10 = pygame.image.load('assets/cards/10_of_clubs.png')
        self.club10 = pygame.transform.scale(club10, (120, 120)) 

        self.heart10 = pygame.image.load('assets/cards/10_of_hearts.png')
        self.heart10 = pygame.transform.scale(heart10, (120, 120)) 

        self.spade10 = pygame.image.load('assets/cards/10_of_spades.png')
        self.spade10 = pygame.transform.scale(spade10, (120, 120)) 

        self.diamondJ = pygame.image.load('assets/cards/jack_of_diamonds.png')
        self.diamondJ = pygame.transform.scale(diamondJ, (120, 120)) 

        self.clubJ = pygame.image.load('assets/cards/jack_of_clubs.png')
        self.clubJ = pygame.transform.scale(clubJ, (120, 120)) 

        self.heartJ = pygame.image.load('assets/cards/jack_of_hearts.png')
        self.heartJ = pygame.transform.scale(heartJ, (120, 120)) 

        self.spadeJ = pygame.image.load('assets/cards/jack_of_spades.png')
        self.spadeJ = pygame.transform.scale(spadeJ, (120, 120)) 

        self.diamondQ = pygame.image.load('assets/cards/queen_of_diamonds.png')
        self.diamondQ = pygame.transform.scale(diamondQ, (120, 120)) 

        self.clubQ = pygame.image.load('assets/cards/queen_of_clubs.png')
        self.clubQ = pygame.transform.scale(clubQ, (120, 120)) 

        self.heartQ = pygame.image.load('assets/cards/queen_of_hearts.png')
        self.heartQ = pygame.transform.scale(heartQ, (120, 120)) 

        self.spadeQ = pygame.image.load('assets/cards/queen_of_spades.png')
        self.spadeQ = pygame.transform.scale(spadeQ, (120, 120)) 

        self.diamondK = pygame.image.load('assets/cards/king_of_diamonds.png')
        self.diamondK = pygame.transform.scale(diamondK, (120, 120)) 

        self.clubK = pygame.image.load('assets/cards/king_of_clubs.png')
        self.clubK = pygame.transform.scale(clubK, (120, 120)) 

        self.heartK = pygame.image.load('assets/cards/king_of_hearts.png')
        self.heartK = pygame.transform.scale(heartK, (120, 120)) 

        self.spadeK = pygame.image.load('assets/cards/king_of_spades.png')
        self.spadeK = pygame.transform.scale(spadeK, (120, 120)) 

        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

        #win and lose bet
    def win_bet(self):
        self.total += 25

    def lose_bet(self):
        self.total -= 25

        # game endings
    def player_busts(player, dealer, chips):
        self.result_text = Text('PLAYER BUSTS!', 500, 800, 28, BLACK)
        lose_bet()


    def player_wins(player, dealer, chips):
        self.result_text = Text('PLAYER WINS!', 500, 800, 28, BLACK)
        win_bet()


    def dealer_busts(player, dealer, chips):
        self.result_text = Text('DEALER BUSTS!', 500, 800, 28, BLACK)
        win_bet()


    def dealer_wins(player, dealer, chips):
        self.result_text = Text('DEALER WINS!', 500, 800, 28, BLACK)
        lose_bet()


    def push(player, dealer):
        self.result_text = Text('Its a push! Player and Dealer tie!', 500, 800, 28, BLACK)




