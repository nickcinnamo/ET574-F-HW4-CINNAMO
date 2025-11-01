import unittest
from main import Die, DiceGame

class TestDiceGame(unittest.TestCase):

    def test_die_roll_within_range(self):
        die = Die()
        for _ in range(100):
            value = die.roll()
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)

    def test_evaluate_roll_outcomes(self):
        game = DiceGame()
        self.assertEqual(game.evaluate_roll(7), "Win")
        self.assertEqual(game.evaluate_roll(11), "Win")
        self.assertEqual(game.evaluate_roll(2), "Lose")
        self.assertEqual(game.evaluate_roll(12), "Lose")
        self.assertEqual(game.evaluate_roll(5), "Roll Again")

    def test_play_round_output_format(self):
        game = DiceGame()
        rolls, total, result = game.play_round()
        self.assertIsInstance(rolls, list)
        self.assertEqual(len(rolls), 2)
        self.assertEqual(sum(rolls), total)
        self.assertIn(result, ["Win", "Lose", "Roll Again"])

if __name__ == "__main__":
    unittest.main()