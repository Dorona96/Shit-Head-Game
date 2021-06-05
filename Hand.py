import random

import Deck

class Hand:
    def __init__(self):
        self.cover = [] #the three card upside down
        self.reveld =[] #the three card on top
        self.hand=[] # the three card in hand
        
    def deal(self):
        for i in range(3):
            print(i)
