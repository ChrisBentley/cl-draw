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

    def test_print_canvas(self):

        expected_output =   '-------' \
                          '\n|     |' \
                          '\n|     |' \
                          '\n|     |' \
                          '\n|     |' \
                          '\n-------'

        new_canvas = Canvas(5, 4)

        out = StringIO()
        with redirect_stdout(out):
            result = print_canvas(new_canvas)

        output = out.getvalue().strip()

        self.assertEqual(expected_output, output)

    def test_correct_create_canvas(self):

        expected_output = Canvas(20, 4)
        user_input_array = ['c', '20', '4']
        output = validate_and_create_canvas(user_input_array)

        self.assertEqual(expected_output.canvas, output.canvas)

    def test_create_canvas_invalid_coords(self):
        out = StringIO()

        user_input_array = ['c', 'a', '4']
        with redirect_stdout(out):
            output = validate_and_create_canvas(user_input_array)
        self.assertEqual(None, output)

    def test_create_canvas_0_dimension_canvas(self):
        out = StringIO()

        user_input_array = ['c', '0', '0']
        with redirect_stdout(out):
            output = validate_and_create_canvas(user_input_array)
        self.assertEqual(None, output)

    def test_create_canvas_extremely_large(self):
        out = StringIO()

        user_input_array = ['c', '10000', '10000']
        with redirect_stdout(out):
            output = validate_and_create_canvas(user_input_array)
        self.assertEqual(None, output)

    def test_correct_draw_line(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  ' ',  ' ',  ' ', ' ', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5, 5)

        user_input_array = ['L', '4', '1', '4', '4']

        validate_and_draw_line(user_input_array, new_canvas)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_draw_line_invalid_coords(self):
        new_canvas = Canvas(5, 5)

        user_input_array = ['L', 'a', 'b', 'c', 'd']

        with self.assertRaises(Exception) as context:
            validate_and_draw_line(user_input_array, new_canvas)

        self.assertTrue('The values you entered for drawing a line were not valid.'
          in str(context.exception))

    def test_draw_line_off_canvas(self):
        new_canvas = Canvas(5, 5)

        user_input_array = ['L', '-1', '1', '-1', '4']

        with self.assertRaises(Exception) as context:
            validate_and_draw_line(user_input_array, new_canvas)

        self.assertTrue('\nNo line was drawn because the coordinates you have entered'
              ' are not within the canvas.'
          in str(context.exception))

    def test_draw_line_not_a_line(self):
        new_canvas = Canvas(5, 5)

        user_input_array = ['L', '1', '1', '2', '4']

        with self.assertRaises(Exception) as context:
            validate_and_draw_line(user_input_array, new_canvas)

        self.assertTrue('\nNo line was drawn because the coordinates you have entered'
              ' do not create a horizontal or vertical line.'
          in str(context.exception))

    def test_correct_draw_rectangle(self):

        expected_canvas = [[ '-',  '-',  '-',  '-',  '-', '-', '-'],
                           [ '|',  ' ',  'x',  'x',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  ' ',  'x', ' ', '|'],
                           [ '|',  ' ',  'x',  'x',  'x', ' ', '|'],
                           [ '-',  '-',  '-',  '-',  '-', '-', '-'] ]

        new_canvas = Canvas(5, 5)

        user_input_array = ['R', '2', '1', '4', '5']

        validate_and_draw_rectangle(user_input_array, new_canvas)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_draw_rectangle_invalid_coords(self):
        new_canvas = Canvas(5, 5)

        user_input_array = ['R', 'a', 'b', 'c', 'd']

        with self.assertRaises(Exception) as context:
            validate_and_draw_rectangle(user_input_array, new_canvas)

        self.assertTrue('The values you entered for drawing a rectangle were not valid.'
          in str(context.exception))

    def test_draw_rectangle_off_canvas(self):
        new_canvas = Canvas(5, 5)

        user_input_array = ['R', '-1', '1', '-1', '4']

        with self.assertRaises(Exception) as context:
            validate_and_draw_rectangle(user_input_array, new_canvas)

        self.assertTrue('\nNo rectangle was drawn because the coordinates you have entered'
              ' are not within the canvas.'
          in str(context.exception))

    def test_draw_rectangle_not_rectangle(self):
        new_canvas = Canvas(5, 5)

        user_input_array = ['R', '1', '4', '1', '4']

        with self.assertRaises(Exception) as context:
            validate_and_draw_rectangle(user_input_array, new_canvas)

        self.assertTrue('\nNo rectangle was drawn because the coordinates you have entered'
              ' do not create rectangle.'
          in str(context.exception))

    def test_correct_fill_area(self):

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

        new_canvas = Canvas(5, 10)

        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        user_input_array = ['B', '5', '4', 'v']

        validate_and_fill_area(user_input_array, new_canvas)

        self.assertEqual(expected_canvas, new_canvas.canvas)

    def test_fill_area_not_coordinates(self):
        new_canvas = Canvas(5, 10)
        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        user_input_array = ['B', 'a', 'b', 'v']

        with self.assertRaises(Exception) as context:
            validate_and_fill_area(user_input_array, new_canvas)

        self.assertTrue('The values you entered as coordinates were not valid.'
          in str(context.exception))

    def test_fill_area_invalid_colour(self):
        new_canvas = Canvas(5, 10)
        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        user_input_array = ['B', '5', '4', 'x']

        with self.assertRaises(Exception) as context:
            validate_and_fill_area(user_input_array, new_canvas)

        self.assertTrue('\nPlease enter a valid colour.'
              ' (The colour must be 1 character long and cannot be "x", "|" or "-")'
          in str(context.exception))

    def test_fill_area_off_canvas(self):
        new_canvas = Canvas(5, 10)
        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        user_input_array = ['B', '20', '20', 'v']

        with self.assertRaises(Exception) as context:
            validate_and_fill_area(user_input_array, new_canvas)

        self.assertTrue('\nNo fill was attempted because the coordinates you have entered'
              ' are not within the canvas.'
          in str(context.exception))

    def test_fill_area_on_a_line(self):
        new_canvas = Canvas(5, 10)
        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        user_input_array = ['B', '1', '1', 'v']

        with self.assertRaises(Exception) as context:
            validate_and_fill_area(user_input_array, new_canvas)

        self.assertTrue('\nThe coordinates you entered fell on a line'
              ' so no fill was attempted'
          in str(context.exception))


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

        new_canvas = Canvas(5, 5)

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

        new_canvas = Canvas(5, 5)

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

        new_canvas = Canvas(5, 5)

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

        new_canvas = Canvas(5, 10)

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

        new_canvas = Canvas(5, 10)

        new_canvas.draw_rectangle(1, 1, 4, 3)
        new_canvas.draw_rectangle(2, 6, 5, 10)

        new_canvas.fill_area(5, 4, 'v')

        self.assertEqual(expected_canvas, new_canvas.canvas)


if __name__ == '__main__':
    unittest.main()
