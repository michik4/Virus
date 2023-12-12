from Game.Victim.victimDeck import VictimDeck

class Victim(VictimDeck):
    def __init__(self, Players):
       self.victimImun = [0, 0, 0] 
       self.victimInfects = [[0,0,0] for i in range(len(Players))] 
       #head[0] body[1] legs[2]

    def PrintInfect(self):
        print(self.victimInfects)   