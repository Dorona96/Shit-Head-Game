import Card
import Deck
import Player
import Pile
import Hand


class Shithead:
    def __init__(self, players, deck, pile) :
        self.players = players
        self.deck = deck
        self.pile = pile
    
    def loser(self, player):
        print("Player %s - YOU ARE SHIT HEAD! hope you'll be better next time", player)

    
    def winner(self, player):
        player.score += 100
        print("Player %s - YOU ARE THE WINNER! your current score : %d", player, player.score)

    






        


