import random

# Singleton Pattern for Board (Only one instance of Board exists)
class Board:
    _instance = None

    def __new__(cls, size=100, snakes=None, ladders=None):
        if not cls._instance:
            cls._instance = super(Board, cls).__new__(cls)
            cls._instance.size = size
            cls._instance.snakes = snakes if snakes else {}
            cls._instance.ladders = ladders if ladders else {}
        return cls._instance

    def get_new_position(self, position):
        """Checks for snakes or ladders and updates position."""
        if position in self.snakes:
            print(f"Oops! Snake at {position}. Go down to {self.snakes[position]}.")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"Yay! Ladder at {position}. Climb up to {self.ladders[position]}.")
            return self.ladders[position]
        return position

# Strategy Pattern for Dice Rolling
class Dice:
    def roll(self):
        """Default rolling strategy (1 to 6)."""
        return random.randint(1, 6)

# Different Dice strategies (e.g., double dice, weighted dice)
class DoubleDice(Dice):
    def roll(self):
        """Rolls two dice and returns the sum."""
        return random.randint(1, 6) + random.randint(1, 6)

class WeightedDice(Dice):
    def roll(self):
        """Gives higher chances for 5 and 6."""
        return random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 1, 1, 3, 3])[0]

# Factory Pattern for Player Creation
class PlayerFactory:
    @staticmethod
    def create_player(name):
        return Player(name)

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, steps, board):
        """Moves the player and checks for snakes/ladders."""
        new_position = self.position + steps
        if new_position > board.size:
            print(f"{self.name} rolled {steps} but can't move beyond {board.size}.")
            return
        
        print(f"{self.name} moves from {self.position} to {new_position}.")
        self.position = board.get_new_position(new_position)

# Observer Pattern for Event Handling
class GameObserver:
    def update(self, message):
        """Prints game updates (Could be extended for GUI or logging)."""
        print(message)

class Game:
    def __init__(self, players, board, dice_type=Dice()):
        self.players = players
        self.board = board
        self.dice = dice_type
        self.observer = GameObserver()

    def play(self):
        """Game loop handling player turns."""
        while True:
            for player in self.players:
                input(f"{player.name}'s turn! Press Enter to roll the dice...")
                roll = self.dice.roll()
                self.observer.update(f"{player.name} rolled a {roll}.")

                player.move(roll, self.board)

                if player.position == self.board.size:
                    self.observer.update(f"🎉 {player.name} wins! 🎉")
                    return  # End game

# Example Setup
if __name__ == "__main__":
    snakes = {17: 7, 54: 34, 62: 19, 98: 79}
    ladders = {3: 22, 6: 25, 20: 38, 57: 76, 72: 91}

    board = Board(snakes=snakes, ladders=ladders)
    players = [PlayerFactory.create_player("Alice"), PlayerFactory.create_player("Bob")]
    
    game = Game(players, board, dice_type=DoubleDice())  # Use Double Dice strategy
    game.play()
