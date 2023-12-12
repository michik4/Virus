from Game.deck import Deck
from Game.table import Table
from Game.Player.player import Player
from Game.Victim.victim import Victim

Player1 = Player()
Player2 = Player()
Victim1 = Victim()

Players = [Player1, Player2]
mainTable = Table(Players)