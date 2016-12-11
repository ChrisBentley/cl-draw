"""
A canvas class that allows the user to create a canvas of size
x,y and draw on it.
"""

class Canvas(object):

    def __init__(self, w, h):

        # Initialize a canvas of size x by y, filled with spaces
        self.canvas = [[' ' for x in range(w + 2)] for y in range(h + 2)]

        # Fill in the borders of the canvas
        for y in range(h + 2):
            for x in range(w + 2):
                if (x == 0 or x == (w + 1)):
                    self.canvas[y][x] = '|'
                if (y == 0 or y == (h + 1)):
                    self.canvas[y][x] = '-'

    def draw_line(self, x1, y1, x2, y2):

        # Check if drawing a vertical line
        if (x1 == x2):
            # Switch y values so it always draws in one direction
            if y1 > y2:
                temp = y1
                y1 = y2
                y2 = temp

            for y in range(y1, (y2+1)):
                self.canvas[y][x1] = 'x'

        # Check if drawing a horizontal line
        if (y1 == y2):
            # Switch y values so it always draws in one direction
            if x1 > x2:
                temp = x1
                x1 = x2
                x2 = temp

            for x in range(x1, (x2+1)):
                self.canvas[y1][x] = 'x'
