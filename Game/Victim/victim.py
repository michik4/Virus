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
            for val in cards:
                typeCard = Deck.CardKeyType(val)
                
                if(typeCard == 0):
                    self.victim[Deck.CardKeyZone(val)][1] += Deck.CardKeyVal(val)
                elif(typeCard == 1):
                    self.victim[Deck.CardKeyZone(val)][0] -= Deck.CardKeyVal(val)    
                elif(typeCard == 2):
                    self.victim[Deck.CardKeyZone(val)][0] += Deck.CardKeyVal(val)#TYPE 
            return cards
        else:
            raise Exception(f"Victim.SetCards: Unknow Type {cards}")    
    def INFO(self):
        print(f"head = \t{self.head}\nbody = \t{self.body}\nlegs = \t{self.legs}")