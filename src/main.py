import pygame

from src.basicgrid import BasicGrid
from src.snake import UnclePy, Directions

from src.exceptions.grid_exceptions import OutOfCellsBoundError
from src.exceptions.snake_exceptions import SnakeTwistedError

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

CELLS_IN_ROW = 60
CELL_WIDTH = 6
CELL_HEIGHT = 6
MARGIN = 1

FPS = 60


def main():
    grid = BasicGrid(CELL_WIDTH, CELL_HEIGHT, MARGIN, CELLS_IN_ROW)

    pygame.init()

    WINDOW_SIZE = grid.screen_size()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption('UnclePy')

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    snake = UnclePy(grid, RED, FPS, 60)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.direction != Directions.LEFT:
                    snake.direction = Directions.RIGHT
                if event.key == pygame.K_LEFT and snake.direction != Directions.RIGHT:
                    snake.direction = Directions.LEFT
                if event.key == pygame.K_UP and snake.direction != Directions.DOWN:
                    snake.direction = Directions.UP
                if event.key == pygame.K_DOWN and snake.direction != Directions.UP:
                    snake.direction = Directions.DOWN

        try:
            snake.move()
        except (OutOfCellsBoundError, SnakeTwistedError):
            snake = UnclePy(grid, RED, FPS)
            grid.clear()

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        grid.draw(screen, pygame)

        # Limit to 60 frames per second
        clock.tick(FPS)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()