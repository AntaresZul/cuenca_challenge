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
        
    def test_case_five(self):
                chess = Chess(5)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 10)

    def test_case_six(self):
                chess = Chess(6)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 4)

    def test_case_seven(self):
                chess = Chess(7)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 40)

    def test_case_eight(self):
                chess = Chess(8)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 92)

    def test_case_nine(self):
                chess = Chess(9)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 352)
    
    def test_case_ten(self):
                chess = Chess(10)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 724)
    
    def test_case_eleven(self):
                chess = Chess(11)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 2680)
    
    def test_case_twelve(self):
                chess = Chess(12)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 14200)
    
    def test_case_thirteen(self):
                chess = Chess(13)
                result = chess.place_queen(0)
                self.assertEqual(len(chess.solutions), 73712)