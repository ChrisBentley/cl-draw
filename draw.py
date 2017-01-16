#!/usr/bin/env python

"""
Program that creates a canvas of user specified dimensions and provides
functions for the user to draw with.

Author: Chris Bentley
"""

import sys
from canvas import Canvas


def check_user_input(user_input_array):

    valid_commands = ['c', 'l', 'r', 'b', 'q', 'h']

    if (user_input_array[0].lower() in valid_commands):
        return True

    print('The command you have entered is not valid.')
    help_prompt()

    return False


def quit():

    sys.exit("Exiting draw.py.")


def help_prompt():

    print('\nAvailable commands:')
    print('"h" - Displays this help prompt.')
    print('"C w h" - Creates a canvas of width "w" and height "h".')
    print('"C" - Clear the canvas of all lines and colours.')
    print('"L x1 y1 x2 y2" - Creates a new line from (x1,y1) to (x2,y2) Only horizontal and vertical lines are supported.')
    print('"R x1 y1 x2 y2" - Creates a rectangle from upper left corner (x1,y1) to lower right corner (x2,y2).')
    print('"B x y c" - Bucket fill which will fill the area containing the selected pixel (x,y) with the colour "c".')
    print('"Q" - Quits the draw program.\n')


def print_canvas(canvas):

    if (canvas is None):
        return

    print('\n')

    for y in range(canvas.height + 2):
        row_values = ''
        for x in range(canvas.width + 2):
            row_values += canvas.canvas[y][x]
        print(row_values)

    print('\n')


def validate_and_create_canvas(user_input_array, canvas):

    if (len(user_input_array) == 1):
        if canvas is None:
            raise ValueError('\nYou must create a canvas before you can clear it.')
        return Canvas(canvas.width, canvas.height)

    try:
        w = int(user_input_array[1])
        h = int(user_input_array[2])
    except ValueError:
        print('\nThe values you entered for creating a canvas were not valid.')
        return None

    if (w <= 0 or h <= 0):
        print('Please enter canvas values greater than 0.')
        return None

    if (w > 1000 or h > 1000):
        print('Please do not try to break this program by creating a '
              'ridiculously large canvas.')
        return None

    return Canvas(w, h)


def validate_and_draw_line(user_input_array, canvas):
    try:
        x1 = int(user_input_array[1])
        y1 = int(user_input_array[2])
        x2 = int(user_input_array[3])
        y2 = int(user_input_array[4])
    except ValueError:
        raise ValueError('The values you entered for drawing a line were not valid.')

    if (x1 < 1 or x1 > canvas.width or
        y1 < 1 or y1 > canvas.height or
        x2 < 1 or x2 > canvas.width or
        y2 < 1 or y2 > canvas.height):
        raise ValueError('\nNo line was drawn because the coordinates you have entered'
              ' are not within the canvas.')

    if (x1 != x2 and y1 != y2):
        raise ValueError('\nNo line was drawn because the coordinates you have entered'
              ' do not create a horizontal or vertical line.')

    canvas.draw_line(x1, y1, x2, y2)

    return canvas


def validate_and_draw_rectangle(user_input_array, canvas):
    try:
        x1 = int(user_input_array[1])
        y1 = int(user_input_array[2])
        x2 = int(user_input_array[3])
        y2 = int(user_input_array[4])
    except ValueError:
        raise ValueError('The values you entered for drawing a rectangle were not valid.')

    if (x1 < 1 or x1 > canvas.width or
        y1 < 1 or y1 > canvas.height or
        x2 < 1 or x2 > canvas.width or
        y2 < 1 or y2 > canvas.height):
        raise ValueError('\nNo rectangle was drawn because the coordinates you have entered'
              ' are not within the canvas.')

    if (x1 == x2 or y1 == y2):
        raise ValueError('\nNo rectangle was drawn because the coordinates you have entered'
              ' do not create rectangle.')

    canvas.draw_rectangle(x1, y1, x2, y2)

    return canvas


def validate_and_fill_area(user_input_array, canvas):
    try:
        x = int(user_input_array[1])
        y = int(user_input_array[2])
    except ValueError:
        raise ValueError('The values you entered as coordinates were not valid.')

    c = user_input_array[3]

    if (len(c) > 1 or c == 'x' or c == '|' or c == '-'):
        raise ValueError('\nPlease enter a valid colour.'
              ' (The colour must be 1 character long and cannot be "x", "|" or "-")')

    if (x < 1 or x > canvas.width or
        y < 1 or y > canvas.height):
        raise ValueError('\nNo fill was attempted because the coordinates you have entered'
              ' are not within the canvas.')

    if (canvas.canvas[y][x] == 'x'):
        raise ValueError('\nThe coordinates you entered fell on a line'
              ' so no fill was attempted')

    canvas.fill_area(x, y, c)

    return canvas


def main():

    print('\nWelcome to draw.py. For a list of available commands you can type "h".')

    canvas = None

    while(1):

        user_input = input("\nPlease enter a command:")

        user_input_array = user_input.split(' ')

        if (check_user_input(user_input_array) is not True):
            # Restart the while loop if the input wasn't a valid command
            continue

        command = user_input_array[0].lower()

        if (command == 'q'):
            quit()

        if (command == 'h'):
            help_prompt()
            continue

        if (command != 'c' and canvas is None):
            print('You need to create a canvas before you can draw something.')
            continue
        try:
            command_dict = {'c': validate_and_create_canvas,
                            'l': validate_and_draw_line,
                            'r': validate_and_draw_rectangle,
                            'b': validate_and_fill_area}

            canvas = command_dict[command](user_input_array, canvas)

            # if (command == 'c'):
            #     canvas = validate_and_create_canvas(user_input_array, canvas)
            # elif (command == 'l'):
            #     validate_and_draw_line(user_input_array, canvas)
            # elif (command == 'r'):
            #     validate_and_draw_rectangle(user_input_array, canvas)
            # elif (command == 'b'):
            #     validate_and_fill_area(user_input_array, canvas)
        except ValueError as e:
            print(e)
            continue

        print_canvas(canvas)


(__name__ == '__main__' and main())
