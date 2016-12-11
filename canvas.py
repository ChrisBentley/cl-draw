"""
A canvas class that allows the user to create a canvas of size
x,y and draw on it.
"""

class Canvas(object):

    def __init__(self, w, h):

        # initialize a canvas of size x by y, filled with spaces
        self.canvas = [[' ' for x in range(w)] for y in range(h)]
