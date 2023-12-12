from Game.deck import Deck

class Victim:
    def __init__(self):
       #[0]=immun [1]=DMG
       self.head = [0, 0]
       self.body = [0, 0]
       self.legs = [0, 0]
       #head[0] body[1] legs[2]
       self.victim = [self.head, self.body, self.legs] 
    def SetCards(self, cards):
        if(type(cards) == str):
            typeCard = Deck.CardKeyType(cards)
            if(typeCard == 0):
                self.victim[Deck.CardKeyZone(cards)][1] += Deck.CardKeyVal(cards)
            elif(typeCard == 1):
                self.victim[Deck.CardKeyZone(cards)][0] -= Deck.CardKeyVal(cards)    
            elif(typeCard == 2):
                self.victim[Deck.CardKeyZone(cards)][0] += Deck.CardKeyVal(cards)
            return cards    
        elif(type(cards) == list):
            for i, val in enumerate(cards):
                typeCard = Deck.CardKeyType(cards[i])
                
                if(typeCard == 0):
                    self.victim[Deck.CardKeyZone(cards[i])][1] += Deck.CardKeyVal(cards[i])
                elif(typeCard == 1):
                    self.victim[Deck.CardKeyZone(cards[i])][0] -= Deck.CardKeyVal(cards[i])    
                elif(typeCard == 2):
                    self.victim[Deck.CardKeyZone(cards[i])][0] += Deck.CardKeyVal(cards[i])#TYPE 
            return cards
        else:
            raise Exception(f"Victim.SetCards: Unknow Type {cards}")    
    def INFO(self):
        print(f"head = \t{self.head}\nbody = \t{self.body}\nlegs = \t{self.legs}")