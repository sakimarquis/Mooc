# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
winlose = ""
busted = ""

score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        self.str = ''
        for i in self.hand:
            self.str = self.str + str(i) + ' '
        return "Hand contains %s." % self.str

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        self.values = 0
        flag = 0
        for i in self.hand:
            self.values += VALUES.get(i.rank)
            if i.rank == 'A':
                flag = 1
        if flag == 1 and self.values + 10 <= 21:
            return self.values + 10
        return self.values
   
    def draw(self, canvas, pos):
        for i in self.hand:
            i.draw(canvas, pos)
            pos[0] += 50
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                card = Card(i,j)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        self.str = ''
        for i in self.deck:
            self.str = self.str + str(i) + ' '
        return "Deck contains %s." % self.str

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score, winlose, busted
    if in_play == False:
        in_play = True
        busted = ""
        outcome = "Hit or Stand?"
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    else:
        outcome = "New Deal?"
        winlose = "Dealer Win!"
        score -= 1
        in_play = False
        
def hit():
    global outcome, in_play, deck, player_hand, score, winlose, busted
    if in_play:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            busted = "Player Busted"
            winlose = "Dealer Win!"
            outcome = "New Deal?"
            in_play = False
            score -= 1
        
def stand():
    global outcome, in_play, deck, dealer_hand, score, winlose, busted
    if in_play:
        while in_play and dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            busted = "Dealer Busted"
            winlose = "Player Win!"
            outcome = "New Deal?"
            score += 1
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                winlose = "Player Win!"
                score += 1
            else:
                winlose = "Dealer Win!"
                outcome = "New Deal?"
                score -= 1 
        in_play = False

# draw handler    
def draw(canvas):
    canvas.draw_text('Black Jack', (175, 75), 50, 'Black') 
    canvas.draw_text('Dealer', (50, 175), 40, 'White')
    dealer_hand.draw(canvas, [50, 200])
    canvas.draw_text('Player', (50, 375), 40, 'White')
    player_hand.draw(canvas, [50, 400])
    canvas.draw_text(outcome, (250, 350), 50, 'Orange')
    canvas.draw_text("Score: %d" % score, (450, 125), 30, 'White')
    if in_play:
        canvas.draw_image(card_back,[25, 48],[50, 96],[50+26,200+48], [50, 96])
    else:
        canvas.draw_text(winlose, (250, 250), 50, 'Fuchsia')
        canvas.draw_text(busted, (250, 200), 40, 'Red')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
