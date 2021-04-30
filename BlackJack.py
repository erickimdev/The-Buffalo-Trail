import pygame
from pygame.locals import *
from colors import *
import random

total = 1000 #change this to the remaining case the player 

        #initializing cards

diamondA = pygame.image.load('assets/cards/ace_of_diamonds.png')
diamondA = pygame.transform.scale(diamondA, (120, 120)) 

clubA = pygame.image.load('assets/cards/ace_of_clubs.png')
clubA = pygame.transform.scale(clubA, (120, 120)) 

heartA = pygame.image.load('assets/cards/ace_of_hearts.png')
heartA = pygame.transform.scale(heartA, (120, 120)) 

spadeA = pygame.image.load('assets/cards/ace_of_spades.png')
spadeA = pygame.transform.scale(spadeA, (120, 120)) 

diamond2 = pygame.image.load('assets/cards/2_of_diamonds.png')
diamond2 = pygame.transform.scale(diamond2, (120, 120)) 

club2 = pygame.image.load('assets/cards/2_of_clubs.png')
club2 = pygame.transform.scale(club2, (120, 120)) 

heart2 = pygame.image.load('assets/cards/2_of_hearts.png')
heart2 = pygame.transform.scale(heart2, (120, 120)) 

spade2 = pygame.image.load('assets/cards/2_of_spades.png')
spade2 = pygame.transform.scale(spade2, (120, 120)) 

diamond3 = pygame.image.load('assets/cards/3_of_diamonds.png')
diamond3 = pygame.transform.scale(diamond3, (120, 120)) 

club3 = pygame.image.load('assets/cards/3_of_clubs.png')
club3 = pygame.transform.scale(club3, (120,120)) 

heart3 = pygame.image.load('assets/cards/3_of_hearts.png')
heart3 = pygame.transform.scale(heart3, (120, 120)) 

spade3 = pygame.image.load('assets/cards/3_of_spades.png')
spade3 = pygame.transform.scale(spade3, (120, 120)) 

diamond4 = pygame.image.load('assets/cards/4_of_diamonds.png')
diamond4 = pygame.transform.scale(diamond4, (120, 120)) 

club4 = pygame.image.load('assets/cards/4_of_clubs.png')
club4 = pygame.transform.scale(club4, (120, 120)) 

heart4 = pygame.image.load('assets/cards/4_of_hearts.png')
heart4 = pygame.transform.scale(heart4, (120, 120)) 

spade4 = pygame.image.load('assets/cards/4_of_spades.png')
spade4 = pygame.transform.scale(spade4, (120, 120)) 

diamond5 = pygame.image.load('assets/cards/5_of_diamonds.png')
diamond5 = pygame.transform.scale(diamond5, (120, 120)) 

club5 = pygame.image.load('assets/cards/5_of_clubs.png')
club5 = pygame.transform.scale(club5, (120, 120)) 

heart5 = pygame.image.load('assets/cards/5_of_hearts.png')
heart5 = pygame.transform.scale(heart5, (120, 120)) 

spade5 = pygame.image.load('assets/cards/5_of_spades.png')
spade5 = pygame.transform.scale(spade5, (120, 120)) 

diamond6 = pygame.image.load('assets/cards/6_of_diamonds.png')
diamond6 = pygame.transform.scale(diamond6, (120, 120)) 

club6 = pygame.image.load('assets/cards/6_of_clubs.png')
club6 = pygame.transform.scale(club6, (120, 120)) 

heart6 = pygame.image.load('assets/cards/6_of_hearts.png')
heart6 = pygame.transform.scale(heart6, (120, 120)) 

spade6 = pygame.image.load('assets/cards/6_of_spades.png')
spade6 = pygame.transform.scale(spade6, (120, 120)) 

diamond7 = pygame.image.load('assets/cards/7_of_diamonds.png')
diamond7 = pygame.transform.scale(diamond7, (120, 120)) 

club7 = pygame.image.load('assets/cards/7_of_clubs.png')
club7 = pygame.transform.scale(club7, (120, 120)) 

heart7 = pygame.image.load('assets/cards/7_of_hearts.png')
heart7 = pygame.transform.scale(heart7, (120, 120)) 

spade7 = pygame.image.load('assets/cards/7_of_spades.png')
spade7 = pygame.transform.scale(spade7, (120, 120)) 

diamond8 = pygame.image.load('assets/cards/8_of_diamonds.png')
diamond8 = pygame.transform.scale(diamond8, (120, 120)) 

club8 = pygame.image.load('assets/cards/8_of_clubs.png')
club8 = pygame.transform.scale(club8, (120, 120)) 

heart8 = pygame.image.load('assets/cards/8_of_hearts.png')
heart8 = pygame.transform.scale(heart8, (120, 120)) 

spade8 = pygame.image.load('assets/cards/8_of_spades.png')
spade8 = pygame.transform.scale(spade8, (120, 120)) 

diamond9 = pygame.image.load('assets/cards/9_of_diamonds.png')
diamond9 = pygame.transform.scale(diamond9, (120, 120)) 

club9 = pygame.image.load('assets/cards/9_of_clubs.png')
club9 = pygame.transform.scale(club9, (120, 120)) 

heart9 = pygame.image.load('assets/cards/9_of_hearts.png')
heart9 = pygame.transform.scale(heart9, (120, 120)) 

spade9 = pygame.image.load('assets/cards/9_of_spades.png')
spade9 = pygame.transform.scale(spade9, (120, 120)) 

diamond10 = pygame.image.load('assets/cards/10_of_diamonds.png')
diamond10 = pygame.transform.scale(diamond10, (120, 120)) 

club10 = pygame.image.load('assets/cards/10_of_clubs.png')
club10 = pygame.transform.scale(club10, (120, 120)) 

heart10 = pygame.image.load('assets/cards/10_of_hearts.png')
heart10 = pygame.transform.scale(heart10, (120, 120)) 

spade10 = pygame.image.load('assets/cards/10_of_spades.png')
spade10 = pygame.transform.scale(spade10, (120, 120)) 

diamondJ = pygame.image.load('assets/cards/jack_of_diamonds.png')
diamondJ = pygame.transform.scale(diamondJ, (120, 120)) 

clubJ = pygame.image.load('assets/cards/jack_of_clubs.png')
clubJ = pygame.transform.scale(clubJ, (120, 120)) 

heartJ = pygame.image.load('assets/cards/jack_of_hearts.png')
heartJ = pygame.transform.scale(heartJ, (120, 120)) 

spadeJ = pygame.image.load('assets/cards/jack_of_spades.png')
spadeJ = pygame.transform.scale(spadeJ, (120, 120)) 

diamondQ = pygame.image.load('assets/cards/queen_of_diamonds.png')
diamondQ = pygame.transform.scale(diamondQ, (120, 120)) 

clubQ = pygame.image.load('assets/cards/queen_of_clubs.png')
clubQ = pygame.transform.scale(clubQ, (120, 120)) 

heartQ = pygame.image.load('assets/cards/queen_of_hearts.png')
heartQ = pygame.transform.scale(heartQ, (120, 120)) 

spadeQ = pygame.image.load('assets/cards/queen_of_spades.png')
spadeQ = pygame.transform.scale(spadeQ, (120, 120)) 

diamondK = pygame.image.load('assets/cards/king_of_diamonds.png')
diamondK = pygame.transform.scale(diamondK, (120, 120)) 

clubK = pygame.image.load('assets/cards/king_of_clubs.png')
clubK = pygame.transform.scale(clubK, (120, 120)) 

heartK = pygame.image.load('assets/cards/king_of_hearts.png')
heartK = pygame.transform.scale(heartK, (120, 120)) 

spadeK = pygame.image.load('assets/cards/king_of_spades.png')
spadeK = pygame.transform.scale(spadeK, (120, 120)) 

suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
deck = []

card_dict = {'Heart2': heart2,'Heart3': heart3,'Heart4': heart4,'Heart5': heart5,'Heart6': heart6,'Heart7': heart7,'Heart8': heart8,'Heart9': heart9,'Heart10': heart10,'HeartK': heartK,'HeartQ': heartQ,'HeartJ': heartJ,'HeartA': heartA
                ,'Diamond2': diamond2,'Diamond3': diamond3,'Diamond4': diamond4,'Diamond5': diamond5,'Diamond6': diamond6,'Diamond7': diamond7,'Diamond8': diamond8,'Diamond9': diamond9,'Diamond10': diamond10,'DiamondK': diamondK,'DiamondQ': diamondQ,'DiamondJ': diamondJ,'DiamondA': diamondA
                ,'Spade2': spade2,'Spade3': spade3,'Spade4': spade4,'Spade5': spade5,'Spade6': spade6,'Spade7': spade7,'Spade8': spade8,'Spade9': spade9,'Spade10': spade10,'SpadeK': spadeK,'SpadeQ': spadeQ,'SpadeJ': spadeJ,'SpadeA': spadeA
                ,'Club2':club2,'Club3':club3,'Club4':club4,'Club5':club5,'Club6':club6,'Club7':club7,'Club8':club8,'Club9':club9,'Club10':club10,'ClubK':clubK,'ClubQ':clubQ,'ClubJ':clubJ,'ClubA':clubA}
        
card_value_dict = {'Heart2': 2,'Heart3': 3,'Heart4': 4,'Heart5': 5,'Heart6': 6,'Heart7': 7,'Heart8': 8,'Heart9': 9,'Heart10': 10,'HeartK': 10,'HeartQ': 10,'HeartJ': 10,'HeartA': 11
                ,'Diamond2': 2,'Diamond3': 3,'Diamond4': 4,'Diamond5': 5,'Diamond6': 6,'Diamond7': 7,'Diamond8': 8,'Diamond9': 9,'Diamond10': 10,'DiamondK': 10,'DiamondQ': 10,'DiamondJ': 10,'DiamondA': 11
                ,'Spade2': 2,'Spade3': 3,'Spade4': 4,'Spade5': 5,'Spade6':6,'Spade7': 7,'Spade8': 8,'Spade9': 9,'Spade10': 10,'SpadeK': 10,'SpadeQ': 10,'SpadeJ': 10,'SpadeA': 11
                ,'Club2': 2,'Club3':3,'Club4':4,'Club5':5,'Club6':6,'Club7':7,'Club8':8,'Club9':9,'Club10':10,'ClubK':10,'ClubQ':10,'ClubJ':10,'ClubA':11}

#creating a deck
for suit in suits:
    for rank in ranks:
        deck.append(suit+rank)

def initGame(cList, uList, dList):#Generates two cards for dealer and user, one at a time for each.Returns if card is Ace and the total amount of the cards per person.'''
    userAces = 0
    dealAces = 0

    random.shuffle(deck)

    Usercard1 =  deck.pop()
    cList.remove(Usercard1)
    uList.append(Usercard1)
    if card_value_dict[Usercard1] == 11:
        userAces += 1

    Usercard2 =  deck.pop()
    cList.remove(Usercard2)
    uList.append(Usercard2)
    if card_value_dict[Usercard2] == 11:
        userAces += 1
    
    random.shuffle(deck)

    DealerCard1 =  deck.pop()
    cList.remove(DealerCard1)
    dList.append(DealerCard1)
    if card_value_dict[DealerCard1] == 11:
        dealAces += 1

    DealerCard2 =  deck.pop()
    cList.remove(DealerCard2)
    dList.append(DealerCard2)
    if card_value_dict[DealerCard2] == 11:
        dealAces += 1
    
    return card_value_dict[Usercard1] + card_value_dict[Usercard2], userAces, card_value_dict[DealerCard1] + card_value_dict[DealerCard2], dealAces

    #Local Variable
duplicatecards = deck.copy()#copy.copy(cards)
stand = False
userCard = []
dealerCard = []
winNum = 0
   
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

#get sums and aces in the initial drawn cards
userSum, userA, dealSum, dealA = initGame(duplicatecards, userCard, dealerCard)

    #Fill Background
background = pygame.Surface(screen.get_size())
background.fill(BLACK)

hitButton = pygame.draw.rect(background, GRAY, (900, 400, 80, 35))
standButton = pygame.draw.rect(background, GRAY, (990, 400, 80, 35))


    #game Loop 
while True:
        #checks if game is over
    gameover = False 

    if (userSum >= 21 and userA == 0):
        gameover = True
     
    if len(userCard) == 2 and userSum == 21:
        gameover = True
    elif len(dealerCard) == 2 and dealSum == 21:
        gameover = True

        #background needs to be redisplayed because it gets updated
    winTxt = font.render('Wins: %i' % winNum, 1, WHITE)
    cashTxt = font.render('Balance Cash: %i' % total, 1, WHITE)

        #checks for mouse clicks on buttons
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitButton.collidepoint(pygame.mouse.get_pos()):
                #gives player a card if they don't break blackjack rules
            #player
            card =  deck.pop()
            duplicatecards.remove(card)
            userCard.append(card)
            if card_value_dict[card] == 11:
                userA += 1

            #dealer
            userSum += card_value_dict[card]
            while userSum > 21 and userA > 0:
                userA -= 1
                userSum -= 10

        elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standButton.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
            stand = True
            while dealSum <= userSum and dealSum < 20:
               #for players
                card =  deck.pop()
                duplicatecards.remove(card)
                dealerCard.append(card)
                if card_value_dict[card] == 11:
                    dealA += 1
                
                #for dealer
                dealSum += card_value_dict[card]
                while dealSum > 21 and dealA > 0:
                    dealA -= 1
                    dealSum -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartButton.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
            if userSum == dealSum:
                pass
            elif userSum <= 21: 
                winNum += 1
                total += 25
            elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                winNum += 1
                total +=25
            else:
                total -=25

            gameover = False
            stand = False
            userCard = []
            dealerCard = []
            duplicatecards = deck.copy()
            userSum, userA, dealSum, dealA = initGame(duplicatecards, userCard, dealerCard)

            restartButton = pygame.draw.rect(background, BLACK, (270, 225, 75, 25))

    #EVERYTHING BELOW COMES IN DRAW FUNCTION

    screen.blit(background, (0, 0))

    screen.blit(gametxt, (600, 0))
    screen.blit(dealerTxt, (660, 100))
    screen.blit(playerTxt,(660, 400))

    screen.blit(hitTxt, (910, 400))
    screen.blit(standTxt, (990, 400))
    screen.blit(winTxt, (220, 575))
    screen.blit(cashTxt, (900,20))

    screen.blit(glitchTxt, (20,130))
    
    

        #displays dealer's cards
    x1 =550
    for card in dealerCard:
        screen.blit(card_dict[card], (x1, 200))
        x1 = x1 + 150

        #displays player's cards
    x2 = 550
    for card in userCard:
        screen.blit(card_dict[card], (x2, 500))
        x2 = x2 + 150

        #when game is over, draws restart button and text, and shows the dealer's second card
    if gameover or stand:
        screen.blit(gameoverTxt, (240, 380))
        restartButton = pygame.draw.rect(background, GRAY, (270, 325, 100, 35))
        screen.blit(restartTxt, (275, 323))
        screen.blit(card_dict[dealerCard[1]], (120, 10))
            
    pygame.display.update()
            


