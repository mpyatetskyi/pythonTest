from random import shuffle
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10,'King':10, 'Ace':11}

playing = True

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +='\n' + card.__str__()

        return 'The deck has' + deck_comp

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():

    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet



def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please insert an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry you dont have enough money. You have {}'.format(chips.total))
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Hit or stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print('Player stands, deallers turn')
            playing = False
        else:
            print('Sorry i dont understand.')
            continue
        break


def show_some(player,dealer):
    print('Dealers hand')
    print('One card hidden')
    print(dealer.cards[1])
    print('\n')
    print('Players hand')
    for card in player.cards:
        print(card)
    print(player.value)

def show_all(player,dealer):
    print('Dealers hand')
    for card in dealer.cards:
        print(card)
    print(dealer.value)
    print('\n')
    print('Players hand')
    for card in player.cards:
        print(card)
    print(player.value)


def player_busts(player,dealer,chips):
    print('Bust Player')
    chips.loose_bet()
def player_wins(player,dealer,chips):
    print('Player wins')
    chips.win_bet()
def dealer_busts(player,dealler,chips):
    print('Player wins, Dealer Busted')
    chips.win_bet()
def dealer_wins(player,dealler,chips):
    print('Dealer wins')
    chips.loose_bet()
def push(player,dealler,chips):
    print('Dealer and player TIE')






while True:
    # Print an opening statement
    print('WELCOME TO BLACKJACK')

    #Create and shuffle the deck, deal two cards for each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Set up players chips
    player_chips = Chips()

    #prompt the player for the bet
    take_bet(player_chips)

    #Show cards
    show_some(player_hand,dealer_hand)

    while playing:
        # ask player hit or stand
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        #player wins or busts
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand,player_chips)

    print('\n Players total chips are at {}'.format(player_chips.total))


    new_game = input('Would you like to play again? Y or N')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break

