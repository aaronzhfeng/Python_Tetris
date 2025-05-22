import unittest

from tetris.src.board import Board
from tetris.src.tetromino import SHAPES

class BoardTest(unittest.TestCase):
    def test_valid_position(self):
        board = Board()
        shape = SHAPES['O'][0]
        self.assertTrue(board.valid_position(shape, 0, 0))
        self.assertFalse(board.valid_position(shape, -1, 0))

    def test_lock_and_clear(self):
        board = Board()
        shape = SHAPES['I'][0]
        # lock four rows to trigger a clear
        for y in range(0, 4):
            board.lock(shape, 0, y, 'I')
        cleared = board.clear_lines()
        self.assertGreaterEqual(cleared, 1)

if __name__ == '__main__':
    unittest.main()
