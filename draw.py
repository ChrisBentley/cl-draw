#!/usr/bin/env python

"""
Program that creates a canvas of user specified dimensions and provides
functions for the user to draw with.

Author: Chris Bentley
"""

import sys
from canvas import Canvas


def check_user_input(user_input_array):

    valid_commands = ['c', 'l', 'r', 'b', 'q']

    if (user_input_array[0].lower() in valid_commands):
        return True

    print('The command you have entered is not valid.')
    help_prompt()

    return False

def quit():

    sys.exit("Exiting draw.py.")

def help_prompt():

    print('\nAvailable commands:')
    print('"C w h" - Creates a canvas of width "w" and height "h".')
    print('"L x1 y1 x2 y2" - Creates a new line from (x1,y1) to (x2,y2) Only horizontal and vertical lines are supported.')
    print('"R x1 y1 x2 y2" - Creates a rectangle from upper left corner (x1,y1) to lower right corner (x2,y2).')
    print('"B x y c" - Bucket fill which will fill the area containing the selected pixel (x,y) with the colour "c".')
    print('"Q" - Quits the draw program.\n')

def print_canvas(canvas):

    if (canvas == None):
        return

    print('\n')

    for y in range(canvas.height):
        for x in range(canvas.width):
            print(canvas.canvas[y][x])
        print('\n')

    print('\n')

def validate_and_create_canvas(user_input_array):
    pass

def validate_and_draw_line(user_input_array):
    pass

def validate_and_draw_rectangle(user_input_array):
    pass

def validate_and_fill_area(user_input_array):
    pass


def main():

    print('\nWelcome to draw.py. For a list of available commands you can type "help" or "h".')

    canvas = None

    while(1):

        user_input = input("\nPlease enter a command:")

        user_input_array = user_input.split(' ')

        if (check_user_input(user_input_array) != True):
            # Restart the while loop if the input wasn't a valid command
            continue

        command = user_input_array[0].lower()

        if (command == 'q'):
            quit()

        if (command != 'c' and canvas == None):
            print('You need to create a canvas before you can draw something.')
            continue

        if (command == 'c'):
            canvas = validate_and_create_canvas(user_input_array)
        elif (command == 'l'):
            validate_and_draw_line(user_input_array)
        elif (command == 'r'):
            validate_and_draw_rectangle(user_input_array)
        elif (command == 'b'):
            validate_and_fill_area(user_input_array)

        print_canvas(canvas)


(__name__ == '__main__' and main())