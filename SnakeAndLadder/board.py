from dice import Dice
from player import Player
class Board:
    def __init__(self):
        self.players = []
        self.snakeAndLadder = {}
        
    def addPlayer(self, player):
        self.players.append(player)
    
    def addSnakeAndLadder(self, start, end):
        self.snakeAndLadder[start] = end
    def start(self):
        """
        1. Iterate through all the player.
        2. Game will stop once a player reached to 100
        3. After rolling dice check whether player is sitting on snake or ladder
        4. Move player to new Position
        """
        while True:
            dice = Dice()
            for player in self.players:
                diceVal = dice.rollDice()
                currentPosition = player.getPosition() + diceVal
                if currentPosition in self.snakeAndLadder:
                    currentPosition = self.snakeAndLadder[currentPosition]
                
                player.setPosition(currentPosition)
                if player.getPosition() == 100:
                    return f"{player.name} is winner"

           
player1 = Player(1, "player1")
player2 = Player(2, "player2")
player3 = Player(3, "player3")
player4 = Player(4, "player4")

board = Board()
board.addPlayer(player1)
board.addPlayer(player2)
board.addPlayer(player3)
board.addPlayer(player4)
board.addSnakeAndLadder(10,30)
board.addSnakeAndLadder(80,20)
print(board.start())
