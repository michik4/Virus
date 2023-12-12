from Game.Player.player import Player
from Game.Victim.victim import Victim

class Table:
    def __init__(self, Players) -> None:
        for i, player in enumerate(Players):
            if(type(player) != Player):
                raise Exception(f"Table.__init__(): Players[{i}]: Unknow Type ({type(player)})") 
        self.Players = Players  