#!/usr/bin/env python

import unittest
from canvas import Canvas
from draw import *
from io import StringIO
from contextlib import redirect_stdout


class TestDraw(unittest.TestCase):

    def test_correct_check_user_input(self):
        correct_user_input_array = ['c', '20', '4']

        self.assertTrue(check_user_input(correct_user_input_array))

    def test_incorrect_check_user_input(self):

        incorrect_user_input_array = ['v', '20', '4']

        out = StringIO()
        with redirect_stdout(out):
            result = check_user_input(incorrect_user_input_array)

        self.assertFalse(result)


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