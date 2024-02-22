"""
    Ameya Santosh Gidh

    This program is the graphics for the puzzle slider game. It draws the
    splashscreen, board, buttons, lose, win, and quit screens
"""
import time
import turtle


class BoardLayout:
    """
    Class: BoardLayout
    Attributes:
    Functions: splash_screen, window_setup, puzzle_box, leaderboard_box,
    control_box, player_moves, control_buttons, run_graphics, lose, win,
    quit_button.
    """
    def __init__(self):
        """
        Constructor -- Creates new instances of wn and pen.
        """
        self.wn = turtle.Screen()
        self.pen = turtle.Turtle()
        self.pen.speed("fastest")
        self.pen.hideturtle()
        self.pen.pensize(5)

    def splash_screen(self):
        """
        Function -- splash_screen
        Creates splashscreen.
        """
        self.wn = turtle.Screen()
        self.wn.bgpic("Resources/splash_screen.gif")
        self.wn.update()
        time.sleep(1)
        self.wn.bgpic("")

    def window_setup(self):
        """
        Function -- window_setup
        This code snippet creates a title for the window
        and defines its dimensions and color.
        """
        self.wn.setup(800, 800)
        self.wn.title("Puzzle Game! by Ameya Santosh Gidh")
        self.wn.bgcolor("LightBlue")

    def puzzle_box(self):
        """
        Function -- puzzle_box
        This code snippet establishes the box outline for the
        puzzle section.
        """
        self.pen.up()
        self.pen.goto(-330, 330)  # top left corner
        self.pen.down()
        self.pen.goto(-330, -150)  # bottom left corner
        self.pen.goto(100, -150)  # bottom right corner
        self.pen.goto(100, 330)  # top right corner
        self.pen.goto(-330, 330)  # Home top left corner
        self.pen.up()

    def leaderboard_box(self):
        """
        Function -- leaderboard_box
        This code segment outlines the leaderboard section
        and displays the label "Leaderboard" at the top.
        """
        self.pen.color("red")
        self.pen.up()
        self.pen.goto(125, 330)  # top left corner
        self.pen.down()
        self.pen.goto(125, -150)  # bottom left corner
        self.pen.goto(330, -150)  # bottom right corner
        self.pen.goto(330, 330)  # top right corner
        self.pen.goto(125, 330)  # Home top left corner
        self.pen.up()
        self.pen.goto(130, 330)
        self.pen.write("Leaderboard:", font=("helvetica", 20, "normal"))

    def control_box(self):
        """
        Function -- control_box
        This code snippet constructs the outline for the
        control box section.
        """
        self.pen.pensize(5)
        self.pen.color("black")
        self.pen.up()
        self.pen.goto(-330, -180)  # top left corner
        self.pen.down()
        self.pen.goto(-330, -350)  # bottom left corner
        self.pen.goto(330, -350)  # bottom right corner
        self.pen.goto(330, -180)  # top right corner
        self.pen.goto(-330, -180)  # Home top left corner
        self.pen.up()

    def player_moves(self):
        """
        Function -- player_moves
        This code writes out the player moves in the control box.
        """
        self.pen.up()
        self.pen.goto(-320, -280)
        self.pen.write(f"Player Moves:", font=("helvetica", 30, "normal"))
        self.pen.up()

    def control_buttons(self):
        """
        Function --control_buttons
        This code utilizes the turtle module to imprint control
        buttons for Load, Reset, and Quit.
        """
        load_button_gif = "Resources/loadbutton.gif"
        reset_button_gif = "Resources/resetbutton.gif"
        quit_button_gif = "Resources/quitbutton.gif"
        self.wn.addshape(load_button_gif)
        self.wn.addshape(reset_button_gif)
        self.wn.addshape(quit_button_gif)
        #  Load Button
        self.pen.up()
        self.pen.goto(80, -270)
        self.pen.shape(load_button_gif)
        self.pen.stamp()
        #  Reset Button
        self.pen.goto(180, -270)
        self.pen.shape(reset_button_gif)
        self.pen.stamp()
        #  Quit Button
        self.pen.goto(280, -270)
        self.pen.shape(quit_button_gif)
        self.pen.stamp()

    def run_graphics(self):
        """
        Function -- run_graphics
        This function is employed to compact board graphics
        and generate the game board.
        """
        self.puzzle_box()
        self.leaderboard_box()
        self.control_box()
        self.player_moves()
        self.control_buttons()

    def lose(self):
        """
        Function -- lose
        This function generates a screen that will be displayed
        when the player loses the game.
        """
        self.wn.clear()
        self.wn.bgcolor("red")
        self.wn.bgpic("Resources/Lose.gif")
        self.wn.update()
        time.sleep(3)
        turtle.bye()

    def win(self):
        """
        Function -- win
        This code creates the screen that will appear when
        the player wins the game.
        """
        self.wn.clear()
        self.wn.bgcolor("green")
        self.wn.bgpic("Resources/winner.gif")
        self.wn.update()
        time.sleep(3)
        turtle.bye()

    def quit_button(self):
        """
        Function -- quit_button
        This code generates a screen that will be displayed
        when the player presses the quit button.
        """
        self.wn.clear()
        self.wn.bgcolor("purple")
        self.wn.bgpic("Resources/quitmsg.gif")
        self.wn.update()
        time.sleep(3)
        turtle.bye()
