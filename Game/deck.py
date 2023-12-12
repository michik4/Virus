from random import randint

class Deck:
    # Card Type = [0]
    #    Type 0 - infect
    #    Type 1 - resist
    #    Type 2 - immun 

    # Card Zone = [1]
    #    Zone 0 - head
    #    Zone 1 - body          
    #    Zone 2 - legs 

    #Card Val = [2]
    
    @staticmethod 
    def CardKeyGen(value = 1, Player = None, typeCard = None, zoneCard = None, valCard = None):
        c = 0 
        retCards = []
        while(c < value):
            key = ""
            form = [typeCard, zoneCard, valCard]
            isList = (value > 1)
            for i in range(len(form)):
                match i:
                    case 0:
                        if(typeCard == None): form[i] = randint(0,2)
                        else: form[i] = typeCard
                    case 1:
                        if(zoneCard == None): form[i] = randint(0,2)
                        else: form[i] = zoneCard    
                    case 2:
                        if(valCard == None): form[i] = randint(0,25) + 0
                        else: form[i] = valCard   
                            
            for i in range(len(form)):    
                key = key + str(form[i]) + "x"
            if(isList):
                retCards.append(key)
            else: 
                return key 
            c += 1
        return retCards
    
    @staticmethod
    def CardKeyTranscript(key):
        transcript = []
        temp = ""

        for i in range(len(key)):
            if key[i] != "x":
                temp = temp + key[i]
            else:
                transcript.append(int(temp))
                temp = ""

        return list(transcript)

    @staticmethod
    def CardKeyType(key):
        transcript = Deck.CardKeyTranscript(key)
        return int(transcript[0])
    @staticmethod 
    def CardKeyZone(key):
        transcript = Deck.CardKeyTranscript(key)
        return int(transcript[1])
    @staticmethod
    def CardKeyVal(key):
        transcript = Deck.CardKeyTranscript(key)
        return int(transcript[2])

    @staticmethod
    def PrintCard(card):
        print(f"type card \t= \t{Deck.CardKeyType(card)}\nzone card \t= \t{Deck.CardKeyZone(card)}\nval card \t= \t{Deck.CardKeyVal(card)}")  
