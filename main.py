import random

class Die:
    def __init__(self, sides=6):
        self.num_sides = sides

    def roll(self):
        return random.randint(1, self.num_sides)

class DiceGame:
    def __init__(self):
        self.dice = [Die(), Die()]

    def evaluate_roll(self, total):
        outcomes = {
            "Win": [7, 11],
            "Lose": [2, 3, 12]
        }
        for result, numbers in outcomes.items():
            if total in numbers:
                return result
        return "Roll Again"

    def play_round(self):
        rolls = [die.roll() for die in self.dice]
        total = sum(rolls)
        result = self.evaluate_roll(total)
        return rolls, total, result

def main():
    game = DiceGame()
    playing = True

    while playing:
        print("\n=== Dice Game Menu ===")
        print("1) Roll Dice")
        print("2) Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            rolls, total, result = game.play_round()
            print(f"Dice rolled: {rolls[0]} and {rolls[1]}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == "2":
            print("Exiting game. Goodbye!")
            playing = False
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()