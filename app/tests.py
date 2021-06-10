from unittest import TestCase
from .app import Chess

class TryTesting(TestCase):
    def test_case_zero(self):
        chess = Chess(0)
        result = chess.place_queen(0)
        self.assertEqual(len(chess.solutions), 0)

    def test_case_one(self):
        chess = Chess(1)
        result = chess.place_queen(0)
        self.assertEqual(len(chess.solutions), 1)
    
    def test_case_two(self):
        chess = Chess(2)
        result = chess.place_queen(0)
        self.assertEqual(len(chess.solutions), 0)

    def test_case_three(self):
            chess = Chess(3)
            result = chess.place_queen(0)
            self.assertEqual(len(chess.solutions), 0)

    def test_case_four(self):
                chess = Chess(4)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 2)