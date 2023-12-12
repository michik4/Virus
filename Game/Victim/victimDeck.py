from Game.deck import Deck
class VictimDeck:
    def SetCards(self, cards, playerCount):
        if(type(cards) == list):
            for i, val in enumerate(cards):
                typeCard = Deck.CardKeyType(val)
                
                if(typeCard == 0):
                    self.victimInfect[playerCount][Deck.CardKeyZone(val)] += Deck.CardKeyVal(val)
                elif(typeCard == 1):
                    self.victimImun[Deck.CardKeyZone(val)] -= Deck.CardKeyVal(val)    
                elif(typeCard == 2):
                    self.victimImun[Deck.CardKeyZone(val)] += Deck.CardKeyVal(val) 
            return cards
        if(type(cards) == str):
            typeCard = Deck.CardKeyType(cards)
            if(typeCard == 0):
                self.victimInfects[playerCount][Deck.CardKeyZone(cards)] += Deck.CardKeyVal(cards)
            elif(typeCard == 1):
                self.victimImun[Deck.CardKeyZone(cards)] -= Deck.CardKeyVal(cards)    
            elif(typeCard == 2):
                self.victimImun[Deck.CardKeyZone(cards)] += Deck.CardKeyVal(cards)
            return cards    
        else:
            raise Exception(f"Victim.SetCards: Cards: Unknow Type {cards}")    
    def INFO(self):
        print(f"head = \t{self.victimImun[0]}\t|\t{self.victimInfects[0]}\nbody = \t{self.victimImun[1]}\t|\t{self.victimInfects[1]}\nlegs = \t{self.victimImun[2]}\t|\t{self.victimInfects[2]}")