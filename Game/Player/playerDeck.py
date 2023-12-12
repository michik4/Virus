from Game.deck import Deck

class PlayerDeck:
    def __init__(self):
        self.playerCards = []

    def GetCardsFromDeck(self, unique = 1 ):
            if(unique == "start"):
                unique = 6
            counter = 0
            cards = []
            while(counter < unique):
                cards.append(Deck.CardKeyGen(1,))
                counter+=1
            for i in range(len(cards)):
                self.playerCards.append(cards[i])
            return cards 

    
    def PostCard(self, index):
        card = self.playerCards[index]
        self.playerCards.pop[index]
        return card
    
    def LenPlayerDeck(self):
        return len(self.playerCards)
    