import pygame
from pygame.locals import *
import random
import copy

#Load Images

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


#Global Constants
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def getAmt(card):
    ''' Returns the amount the card is worth.
E.g. Ace is default 11. 10/Jack/Queen/King is 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print ('getAmt broke')
        exit()

def genCard(cList, xList):
    '''Generates an card from cList, removes it from cList, and appends it to xList.
Returns if card is Ace and the card itself.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Generates two cards for dealer and user, one at a time for each.
Returns if card is Ace and the total amount of the cards per person.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA

def main():
    #Local Variable
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0
   
    #Initialize Game
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Restart', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))
    hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
    standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))
    ratioB = pygame.draw.rect(background, gray, (555, 420, 75, 50))

    #Event Loop
    while True:
        #checks if game is over
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        #background needs to be redisplayed because it gets updated
        winTxt = font.render('Wins: %i' % winNum, 1, black)
        loseTxt = font.render('Losses: %i' % loseNum, 1, black)

        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                #gives player a card if they don't break blackjack rules
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    winNum += 1
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    winNum += 1
                else:
                    loseNum += 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))

        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (39, 448))
        screen.blit(standTxt, (116, 448))
        screen.blit(winTxt, (565, 423))
        screen.blit(loseTxt, (565, 448))

        #displays dealer's cards
        for card in dealCard:
            x = 10 + dealCard.index(card) * 110
            screen.blit(card, (x, 10))
        

        #displays player's cards
        for card in userCard:
            x = 10 + userCard.index(card) * 110
            screen.blit(card, (x, 295))

        #when game is over, draws restart button and text, and shows the dealer's second card
        if gameover or stand:
            screen.blit(gameoverTxt, (270, 200))
            restartB = pygame.draw.rect(background, gray, (270, 225, 75, 25))
            screen.blit(restartTxt, (287, 228))
            screen.blit(dealCard[1], (120, 10))
            
        pygame.display.update()
            

if __name__ == '__main__':
    main()