from typing import List, Optional

from .settings import COLUMNS, ROWS

class Board:
    def __init__(self):
        self.grid: List[List[Optional[str]]] = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

    def inside(self, x: int, y: int) -> bool:
        return 0 <= x < COLUMNS and 0 <= y < ROWS

    def empty(self, x: int, y: int) -> bool:
        return self.inside(x, y) and self.grid[y][x] is None

    def valid_position(self, shape: List[List[int]], x: int, y: int) -> bool:
        for dy, row in enumerate(shape):
            for dx, cell in enumerate(row):
                if cell:
                    if not self.empty(x + dx, y + dy):
                        return False
        return True

    def lock(self, shape: List[List[int]], x: int, y: int, color: str):
        for dy, row in enumerate(shape):
            for dx, cell in enumerate(row):
                if cell and self.inside(x + dx, y + dy):
                    self.grid[y + dy][x + dx] = color

    def clear_lines(self) -> int:
        cleared = 0
        new_grid = [row for row in self.grid if any(c is None for c in row)]
        cleared = ROWS - len(new_grid)
        while len(new_grid) < ROWS:
            new_grid.insert(0, [None for _ in range(COLUMNS)])
        self.grid = new_grid
        return cleared
