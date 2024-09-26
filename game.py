import random

from dataclasses import dataclass, field

@dataclass
class FruitRoller:
    starting_amount: float = 1.00
    balance: float = field(init=False)
    symbols: list[str] = field(default_factory=lambda: ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"])
    bell_sets: int = 0
    skull_sets: int = 0

    def __post_init__(self):
        self.balance = self.starting_amount

        
    def fruit_roller(self) -> None:
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
        self.balance -= 0.20
        print(f"£{self.balance:.2f}")
        rolled_symbol: str = self.roll_fruit()
        self.get_loss_or_gains(rolled_symbol)

    def roll_fruit(self) -> None:
        rolled_symbol: str = random.choice(self.symbols)
        print(rolled_symbol)
        return rolled_symbol

    def get_loss_or_gains(self, rolled_symbol: str) -> None:
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
