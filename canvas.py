"""
A canvas class that allows the user to create a canvas of size
x,y and draw on it.
"""

class Canvas(object):

    def __init__(self, w, h):

        self.width = w
        self.height = h

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
                y1, y2 = y2, y1

            for y in range(y1, (y2+1)):
                self.canvas[y][x1] = 'x'

        # Check if drawing a horizontal line
        if (y1 == y2):
            # Switch y values so it always draws in one direction
            if x1 > x2:
                x1, x2 = x2, x1

            for x in range(x1, (x2+1)):
                self.canvas[y1][x] = 'x'

    def draw_rectangle(self, x1, y1, x2, y2):
        # Draw the top horizontal line
        self.draw_line(x1, y1, x2, y1)
        # Draw the bottom horizonal line
        self.draw_line(x1, y2, x2, y2)
        # Draw the left side vertical line
        self.draw_line(x1, y1, x1, y2)
        # Draw the right side vertical line
        self.draw_line(x2, y1, x2, y2)

    def fill_area(self, x, y, c):
        self.colour = c
        self.coordinates_stack = []
        self.coordinates_stack.append([x,y])

        while (len(self.coordinates_stack) > 0):
            for coords in self.coordinates_stack:
                self.check_coords(coords)
                self.coordinates_stack.remove(coords)

    def check_coords(self, coords):
        x = coords[0]
        y = coords[1]

        if (x < 1 or x > self.width):
            return
        if (y < 1 or y > self.height):
            return

        if (self.canvas[y][x] != '-' and
            self.canvas[y][x] != '|' and
            self.canvas[y][x] != 'x' and
            self.canvas[y][x] != self.colour):
            self.canvas[y][x] = self.colour
            self.coordinates_stack.append([(x+1),y])
            self.coordinates_stack.append([(x-1),y])
            self.coordinates_stack.append([x,(y+1)])
            self.coordinates_stack.append([x,(y-1)])

        return
