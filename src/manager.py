import pygame

from src.config import CELL_WIDTH, CELL_HEIGHT, MARGIN, CELLS_IN_ROW, FPS
from src.exceptions.grid_exceptions import OutOfGridBoundsError
from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError, SnakeBackwardMoveError
from src.grid.grid import BasicGrid
from src.snake import Directions, UnclePy


class GameManager:
    def __init__(self):
        self.grid = BasicGrid(
            grid_info=(CELL_WIDTH, CELL_HEIGHT, MARGIN),
            grid_bounds=(CELLS_IN_ROW, CELLS_IN_ROW)
        )

        pygame.init()

        window_size = self.grid.screen_size()
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('UnclePy')

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def dispose(self):
        self.grid.clear()

        self.snake = UnclePy(
            grid=self.grid,
            cell=self.grid.get_cell(CELLS_IN_ROW - 4, 0),
            length=3,
            color=(255, 0, 0),
        )

        self.grid.add_food((100, 100, 0), 3)
        self.grid.add_food((100, 100, 0), 3)

    def start(self):
        frame_counter = 0

        self.dispose()
        self.grid.draw(self.screen, pygame)
        pygame.display.flip()

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_RIGHT:
                            self.snake.direction = Directions.RIGHT
                        if event.key == pygame.K_LEFT:
                            self.snake.direction = Directions.LEFT
                        if event.key == pygame.K_UP:
                            self.snake.direction = Directions.UP
                        if event.key == pygame.K_DOWN:
                            self.snake.direction = Directions.DOWN
                    except SnakeBackwardMoveError:
                        pass
            try:
                if frame_counter < (FPS - 1) / self.snake.speed:
                    frame_counter += 1
                else:
                    self.snake.move()
                    frame_counter = 0
            except (OutOfGridBoundsError, SnakeTwistedError, SnakeHeadBeatenError):
                # print(f'Total scores {self.snake.scores}')
                break

            self.grid.draw(self.screen, pygame)

            self.clock.tick(500)
            pygame.display.flip()


