# Command Line Draw Tool
A command line drawing tool which allows the user to draw lines, rectangles & fill in areas (Additional functionality TBD).

Developed using Python 3.5.5

Install the requirements using

    $ pip install -U -r requirements.txt

Run the drawing tool using using the following:

    $ ./draw.py

Run the tests using:

    $ ./tests.py


Design Decisions:

My first thoughts are that I will make the canvas a class where the functions such as drawing a line or rectangle can be called on the created canvas. This will allow for future improvements to the drawing program such as having multiple canvas' open or saving/loading a previous canvas.

For edge cases and errors my initial thoughts are those of the user trying to input an invalid command, this will require input validation with a safe error handling to return the user to the input prompt. For each method there could be errors with the user entering invalid coordinates, such as negative number or coordinates that fall outside of the canvas. I will also set a maximum canvas size so that the program cannot crash.

When creating a canvas the created array will also have to be two squares larger than specified by the user to accommodate for the outline of the canvas when printing the drawing.

I will also add a help function that will print out the commands available to the user.