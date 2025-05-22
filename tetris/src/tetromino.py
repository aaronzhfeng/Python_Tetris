from dataclasses import dataclass
from typing import List

# Shape definitions for all tetromino types
SHAPES = {
    'I': [
        [[1, 1, 1, 1]],
        [[1], [1], [1], [1]],
    ],
    'O': [
        [[1, 1], [1, 1]],
    ],
    'T': [
        [[0, 1, 0], [1, 1, 1]],
        [[1, 0], [1, 1], [1, 0]],
        [[1, 1, 1], [0, 1, 0]],
        [[0, 1], [1, 1], [0, 1]],
    ],
    'S': [
        [[0, 1, 1], [1, 1, 0]],
        [[1, 0], [1, 1], [0, 1]],
    ],
    'Z': [
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1], [1, 1], [1, 0]],
    ],
    'J': [
        [[1, 0, 0], [1, 1, 1]],
        [[1, 1], [1, 0], [1, 0]],
        [[1, 1, 1], [0, 0, 1]],
        [[0, 1], [0, 1], [1, 1]],
    ],
    'L': [
        [[0, 0, 1], [1, 1, 1]],
        [[1, 0], [1, 0], [1, 1]],
        [[1, 1, 1], [1, 0, 0]],
        [[1, 1], [0, 1], [0, 1]],
    ],
}

@dataclass
class Tetromino:
    shape: str
    rotation: int = 0
    x: int = 3
    y: int = 0

    @property
    def matrix(self) -> List[List[int]]:
        return SHAPES[self.shape][self.rotation % len(SHAPES[self.shape])]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(SHAPES[self.shape])

