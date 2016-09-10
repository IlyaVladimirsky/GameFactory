import unittest

from basicgrid import BasicGrid
from exceptions.bounds import OutOfCellsBoundError

from snake import UnclePy


class BasicGridTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_draw(self):
        self.assertTrue(True)

    def test_set_color_of_cell(self):
        color = (255, 255, 255)
        grid = BasicGrid(20, 20, 5, 10)

        grid.set_color_of_cell(color, 0, 2)
        self.assertTupleEqual(color, grid.get_color_of_cell(0, 2))

    def test_calculate_screen_size(self):
        grid = BasicGrid(20, 20, 5, 10)

        self.assertListEqual([255, 255], grid.calculate_screen_size())

    def test_clear(self):
        grid = BasicGrid(20, 20, 5, 10)
        UnclePy(grid, (255, 0, 0), 60)
        grid.clear()

        for row in grid:
            for cell in row:
                self.assertTupleEqual(grid.default_color, cell)

    def test_grid_init(self):
        grid = BasicGrid(20, 20, 5, 10)._grid

        for row in grid:
            for cell in row:
                self.assertTupleEqual(grid.default_color, cell)

    def test_convert_to_cell_coordinates(self):
        grid = BasicGrid(20, 20, 5, 10)

        self.assertTupleEqual((0, 0), grid.convert_to_cell_coordinates(6, 6))

        try:
            grid.convert_to_cell_coordinates(27, 27)
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail if passed coordinates are between cells')

        try:
            grid.convert_to_cell_coordinates(-5, -20)
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail if passed coordinates are negative')

        try:
            grid.convert_to_cell_coordinates(0, 0)
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail if passed coordinates are zeros')
