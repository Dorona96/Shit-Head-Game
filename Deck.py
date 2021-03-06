import random
import Card

class Deck:
    def _init_(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["♠","♣","♦","♥"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

        self.cards.append(Card('black', 'joker'))
        self.cards.append(Card('red', 'joker'))
       
    
    def show(self):
        for c in self.cards:
            c.show()
    

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def drawCard(self):
        return self.cards.pop()
    


