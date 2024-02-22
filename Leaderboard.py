"""
    Ameya Santosh Gidh

    This program will define the Leaderboard class,
    which will handle tasks such as reading, writing,
    and presenting the players in the leaderboard.
"""

import time
import turtle


class Leaderboard:
    """
    Class: Leaderboard
    Attributes: player_info
    Methods: update_leaderboard, read_leaderboard, sort_leaderboard,
    draw_leaderboard
    """

    def __init__(self, player_info=list):
        """
        Constructor -- Creates leaderboard_turtle to be used in writing
        leaderboard names
        Parameters:
        player_info -- a list which will contain only the current user
        that won
        """
        self.leaderboard_data = None
        self.player_info = player_info
        self.sorted_leaderboard = []
        self.leaderboard_turtle = turtle.Turtle()
        self.leaderboard_turtle.hideturtle()
        self.leaderboard_turtle.speed("fastest")

    def update_leaderboard(self):
        """
        Function --update_leaderboard
        Employed when the player wins the game. It accepts the number
        of moves required and the player's name.
        """
        with open("leaderboard.txt", mode="a") as outfile:
            outfile.write(f"{self.player_info[0]}:{self.player_info[1]}\n")

    def read_leaderboard(self):
        """
        Function -- read_leaderboard
        Utilized to read the leaderboard.txt file for writing the leaderboard.
        If none exists, an error message will appear and the program will close.
        """
        try:
            with open("leaderboard.txt", mode="r") as infile:
                self.leaderboard_data = infile.read().split("\n")
                self.leaderboard_data.pop()
        except FileNotFoundError:
            turtle.Screen().addshape("Resources/leaderboard_error.gif")
            self.leaderboard_turtle.shape("Resources/leaderboard_error.gif")
            self.leaderboard_turtle.showturtle()
            time.sleep(4)
            self.leaderboard_turtle.hideturtle()

    def sort_leaderboard(self):
        """
        Function -- sort_leaderboard
        The Leaderboard data loaded from the leaderboard.txt file is sorted. This is
        achieved by creating a nested list and then using the sorted function to generate
        a new sorted_leaderboard list.
        """
        for player in self.leaderboard_data:
            temp = player.split(":")
            self.sorted_leaderboard.append([int(temp[0]), temp[1]])
        self.sorted_leaderboard = sorted(self.sorted_leaderboard, key=lambda
            x: x[0])

    def draw_leaderboard(self):
        """
        Function -- draw_leaderboard
        This code utilizes turtle to write each move and name in the leaderboard box.
        It is designed to be updated every time the game is relaunched.
        """
        self.leaderboard_turtle.up()
        self.leaderboard_turtle.goto(135, 260)
        self.leaderboard_turtle.right(90)
        for player in self.sorted_leaderboard:
            self.leaderboard_turtle.write(f"{player[0]} : {player[1]}",
                                          font=("helvetica", 15, "normal"))
            self.leaderboard_turtle.forward(20)
