import Hand
class Player:
    def _init_(self,name):
        self.name = name
        self.score = 0
        self.hand = Hand
    
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self
    
    def throw(self,pile,card):
        for i in self.hand:
            if (card == self.hand[i]):
                self.hand.remove(self.hand[i])
               
            
    def showHand(self):
        for card in self.hand:
            card.show()
        
    
    

    