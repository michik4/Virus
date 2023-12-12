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
        main = Game(Players)
        main.Game()

    def __init__(self, Players):
        self.players = Players
        self.victim = Victim(Players)
        self.mainTable = Table(Players, self.victim)

    def Game(self):
        Proc = True
        while(Proc):
            for player in self.players:
                player.GetCardsFromDeck("start")
            self.mainTable.TableInfo()
            card = Deck.CardKeyGen()
            print(card)
            self.victim.SetCards(card, 1)
            self.victim.PrintInfect()
            Proc = False

            

