"""
A canvas class that allows the user to create a canvas of size
x,y and draw on it.
"""

class Canvas(object):

    def __init__(self, w, h):

        # initialize a canvas of size x by y, filled with spaces
        self.canvas = [[' ' for x in range(w + 2)] for y in range(h + 2)]

        # Fill in the borders of the canvas
        for y in range(h + 2):
            for x in range(w + 2):
                if (y == 0 or y == (w + 1)):
                    self.canvas[x][y] = '|'
                if (x == 0 or x == (h + 1)):
                    self.canvas[x][y] = '-'