from random import shuffle
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10,'King':10, 'Ace':10}


class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


#mycard = Card('Hearts','Two')
#print(mycard.value)


class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def rmeove_cards(self):
        self.all_cards.pop()

    def mysum(self,mylist):

        for val,item in mylist:
            mysum = card[val]

        return mysum

deck = Deck()

mydeck = deck.all_cards
print(mydeck)





class Player():

    def __init__(self,name,balance):
        self.my_cards = []
        self.name = name
        self.balance = balance

    def add_money(self,value):
        self.balance = self.balance + value
        print(f'{self.name} put {value} $ on his account')
        return self.balance

    def cashout(self,value):
        if value > self.balance:
            print('You don`t have enough money on your account')
        else:
            self.balance = self.balance - value
        return  self.balance

    def __str__(self):
        return f'{self.name} has {self.balance} $ on his balance!'


    def add_one(self,new_cards):
        self.my_cards.append(new_cards)
