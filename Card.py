class Card(object):
    FACES = {11: 'Jack', 12: 'Queen', 13:'King', 14: 'Ace', 15:'Joker'}

    def __init__(self,value, suit):
           self.suit =suit
           self.value= value
