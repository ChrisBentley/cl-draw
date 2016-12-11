#!/usr/bin/env python

import unittest
from canvas import Canvas


class TestDraw(unittest.TestCase):

    def test_valid_command(self):
        pass


class TestCanvas(unittest.TestCase):

    def test_create_canvas(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5, 4)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_draw_horizontal_line(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  'x',  'x',  'x',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5,5)

        new_canvas.draw_line(1, 2, 3, 2)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_draw_vertical_line(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5,5)

        new_canvas.draw_line(4, 1, 4, 4)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_draw_rectangle(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  ' ',  'x',  'x',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  'x',  'x', ' ', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5,5)

        new_canvas.draw_rectangle(2, 1, 4, 5)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_fill_area_1(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  'x',  'x',  'x',  'x', ' ', '|'],
                           [ '|',  'x',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  'x',  'x',  'x',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '|',  ' ',  'x',  'x',  'x', 'x', '|'],
                           [ '|',  ' ',  'x',  'o',  'o', 'x', '|'],
                           [ '|',  ' ',  'x',  'o',  'o', 'x', '|'],
                           [ '|',  ' ',  'x',  'o',  'o', 'x', '|'],
                           [ '|',  ' ',  'x',  'x',  'x', 'x', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5,10)

        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        new_canvas.fill_area(4, 9, 'o')

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_fill_area_2(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  'x',  'x',  'x',  'x', 'v', '|'],
                           [ '|',  'x',  ' ',  ' ',  'x', 'v', '|'],
                           [ '|',  'x',  'x',  'x',  'x', 'v', '|'],
                           [ '|',  'v',  'v',  'v',  'v', 'v', '|'],
                           [ '|',  'v',  'v',  'v',  'v', 'v', '|'],
                           [ '|',  'v',  'x',  'x',  'x', 'x', '|'],
                           [ '|',  'v',  'x',  ' ',  ' ', 'x', '|'],
                           [ '|',  'v',  'x',  ' ',  ' ', 'x', '|'],
                           [ '|',  'v',  'x',  ' ',  ' ', 'x', '|'],
                           [ '|',  'v',  'x',  'x',  'x', 'x', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5,10)

        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        new_canvas.fill_area(5, 4, 'v')

        self.assertEqual(expected_canvas, new_canvas.canvas)


if __name__ == '__main__':
    unittest.main()