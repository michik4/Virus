from Game.deck import Deck
from Game.table import Table
from Game.Player.player import Player
from Game.Victim.victim import Victim

class Game:
    @staticmethod
    def GameStart():
        print("HOW PLAYERS: ")
        cPlayers = 3 #int(input())
        Players = [Player() for i in range(0,cPlayers)]
        main = Game.__init__(Game, Players)
        main.Game(main)

    def __init__(self, Players):
        self.players = Players
        self.victim = Victim
        self.mainTable = Table(Players, self.victim)
        return self

    def Game(self):
        Proc = True
        while(Proc):
            for player in self.players:
                player.GetCardsFromDeck("start")
            self.mainTable.TableInfo()
            Proc = False

            

