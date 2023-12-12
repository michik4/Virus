from Game.Player.player import Player
from Game.Victim.victim import Victim
from Game.deck import Deck

class Table:
    def __init__(self, Players):
        for i, player in enumerate(Players):
            if(type(player) != Player):
                raise Exception(f"Table.__init__(): Players[{i}]: Type not Player: (obj = {player} type = {type(player)})") 
        self.Players = Players   
        self.mainVictim = Victim() 

    def TableInfo(self):
        for player in self.Players:
            print(player.playerCards)    
        print(self.mainVictim.INFO())    
