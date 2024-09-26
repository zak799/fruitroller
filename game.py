import random
from dataclasses import dataclass, field

@dataclass
class FruitRoller:
    """
    A Game Simulation For a 'Gambling' Fruit Roller. 

    Attributes:
       - starting_amount: Starting amount(float) of money given the player(£1).
       - balance: Stores how much money the user has won or lost, __init__'ed? after start amount has been given.
       - symbols: list, for what the user can roll
       - bell_sets: counts how many consecutive 'Bells' are rolled. - x3 Bells += £5 to balance
       - skull_sets: counts how many consecutive 'skulls' are rolled. - x3 Bells = Reset Balance.
   
       + uses a dataclass instead of using __init__() for automatic method generation(lambda)
         and abilities to set default values and factory functions for mutable values(symbols list).

        + uses field(default_factory=lambda: []) to initialise 
          fields with new mutable values for each object.
      """
    starting_amount: float = 1.00
    balance: float = field(init=False)
    symbols: list[str] = field(default_factory=lambda: ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"])
    bell_sets: int = 0
    skull_sets: int = 0

    def __post_init__(self):
        """Initialises the players balances after the start amount object has been created."""
        self.balance = self.starting_amount

        
    def fruit_roller(self) -> None:
        """
        Initialises the game start; Allows player to 'Roll' or 'Quit'.

        while True loop, to always prompt the player to 'Roll' or 'Quit', halted once they Quit -
        - or Balance falls below £0.20 - The minimum balance allowed to play, any lower = Quits Game -
        - Player cannot afford to roll. And bankrupts the player.
        """
        print("Commands: Quit and Roll")
        commands: list[str] = ["QUIT", "ROLL", ""]
        while True:
            play: str = input("Roll The FruitRoller?: ").upper().strip()
            if play not in commands:
                print("Unknown Text Entry")
                continue
            if play == "ROLL":
                self.roll()
                if self.balance < 0.20:
                    print("You Have Been Bankrupted!")
                    break
            elif play == "QUIT":
                print("\nGoodbye")
                print(f"You Have Left With Your Winnings Of \n£{self.balance:.2f}")
                break

    def roll(self) -> None:
        """
        Proccesses every roll of the fruit roller. subtracts £0.20 from the balance,
        the minimum required to play, also, displays the users balance, and prints the
        roll outcome from the roll_fruit function.
        """
        self.balance -= 0.20
        print(f"£{self.balance:.2f}")
        rolled_symbol: str = self.roll_fruit()
        self.get_loss_or_gains(rolled_symbol)

    def roll_fruit(self) -> None:
        """
        Chooses a random item from the Symbols list. 
        
        And then Returns the random item from the list of symbols
        symbols: ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
        """
        rolled_symbol: str = random.choice(self.symbols)
        print(rolled_symbol)
        return rolled_symbol

    def get_loss_or_gains(self, rolled_symbol: str) -> None:
        """
        updates the users balance, based on outcome of whatever they rolled.
        'Bell': x3 += £5 to balance.
        'Skull': x3 resets balance - bankrupts the user.

        - uses rolled_symbol args to take outcome. 
        """
        if rolled_symbol == "Bell":
            self.bell_sets += 1
            if self.bell_sets == 3:
                print("You Won £5")
                self.balance += 5
                self.bell_sets = 0
            else:
                print(f"Bell count: {self.bell_sets}")
        else:
            self.bell_sets = 0

        if rolled_symbol == "Skull":
            self.skull_sets += 1
            if self.skull_sets == 3:
                print("You Lost Everything!")
                self.balance = 0
                self.skull_sets = 0 
            elif self.skull_sets == 2:
                print("You Lost £1")
                self.balance -= 1
                print(f"Balance: £{self.balance:.2f}")
            else:
                print(f"Skull count: {self.skull_sets}")
        else:
            self.skull_sets: int = 0


if __name__ == "__main__":
    game = FruitRoller()
    game.fruit_roller()
