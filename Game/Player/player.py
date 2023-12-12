from Game.Player.playerDeck import PlayerDeck

class Player(PlayerDeck):
    def __init__(self, VIRUS_NAME = "ex"):
        PlayerDeck.__init__(self)
        self.virusName = VIRUS_NAME
        
        
