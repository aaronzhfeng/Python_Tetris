import random
import pygame

from .settings import COLORS, COLUMNS, ROWS, CELL_SIZE
from .board import Board
from .tetromino import Tetromino, SHAPES
from .utils import draw_text

STATE_MENU = 'MENU'
STATE_PLAYING = 'PLAYING'
STATE_PAUSED = 'PAUSED'
STATE_GAME_OVER = 'GAME_OVER'

class Game:
    def __init__(self):
        self.state = STATE_MENU
        self.board = Board()
        self.current = None
        self.next_piece()
        self.score = 0

    def next_piece(self):
        shape = random.choice(list(SHAPES.keys()))
        self.current = Tetromino(shape)

    def handle_key(self, key):
        if self.state == STATE_MENU and key == pygame.K_RETURN:
            self.state = STATE_PLAYING
        elif self.state == STATE_PLAYING:
            if key == pygame.K_LEFT:
                self.move(-1, 0)
            elif key == pygame.K_RIGHT:
                self.move(1, 0)
            elif key == pygame.K_DOWN:
                self.move(0, 1)
            elif key in (pygame.K_UP, pygame.K_z, pygame.K_x):
                self.rotate()
            elif key == pygame.K_SPACE:
                while self.move(0, 1):
                    pass
                self.lock_piece()
        elif self.state == STATE_GAME_OVER and key == pygame.K_RETURN:
            self.__init__()

    def move(self, dx, dy) -> bool:
        new_x = self.current.x + dx
        new_y = self.current.y + dy
        if self.board.valid_position(self.current.matrix, new_x, new_y):
            self.current.x = new_x
            self.current.y = new_y
            return True
        elif dy:
            self.lock_piece()
        return False

    def rotate(self):
        old_rotation = self.current.rotation
        self.current.rotate()
        if not self.board.valid_position(self.current.matrix, self.current.x, self.current.y):
            self.current.rotation = old_rotation

    def lock_piece(self):
        self.board.lock(self.current.matrix, self.current.x, self.current.y, self.current.shape)
        cleared = self.board.clear_lines()
        self.score += cleared * 100
        self.next_piece()
        if not self.board.valid_position(self.current.matrix, self.current.x, self.current.y):
            self.state = STATE_GAME_OVER

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))
        for y, row in enumerate(self.board.grid):
            for x, cell in enumerate(row):
                if cell:
                    color = COLORS[cell]
                    pygame.draw.rect(surface, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(surface, (0,0,0), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        # draw current piece
        for dy, row in enumerate(self.current.matrix):
            for dx, cell in enumerate(row):
                if cell:
                    x = (self.current.x + dx) * CELL_SIZE
                    y = (self.current.y + dy) * CELL_SIZE
                    pygame.draw.rect(surface, COLORS[self.current.shape], (x, y, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(surface, (0,0,0), (x, y, CELL_SIZE, CELL_SIZE), 1)
        draw_text(surface, f"Score: {self.score}", 5, 5)
        if self.state == STATE_MENU:
            draw_text(surface, "Press Enter to start", 50, 200)
        elif self.state == STATE_GAME_OVER:
            draw_text(surface, "Game Over! Press Enter", 50, 200)
