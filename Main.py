"""
    Ameya Santosh Gidh

    This script acts as the primary controller for the puzzle game,
    initializing all necessary components to enable gameplay. If any errors
    occur during gameplay, they will be logged in the "5001_puzzle.err" file,
    and the game will be terminated.
"""
import turtle

from BoardLayout import BoardLayout
from Leaderboard import Leaderboard
from PuzzleClicks import PuzzleClicks


def player_name():
    """
    Function -- player_name
    This function prompts the user to input their name and returns the name
    entered by the user.
    """
    name = turtle.Screen().textinput("Puzzle Slider", "Enter in your name:")
    return name


def player_moves():
    """
    Function - player_moves:
    This function prompts the user to input the number of moves they want to
    make to solve the puzzle. If the entered number falls outside the acceptable range,
    the prompt will reappear until a valid input is provided.
    Returns: The desired number of moves specified by the user.
    """
    moves = 0
    while moves < 5 or moves > 200:
        moves = int(turtle.Screen().textinput("Puzzle Slider - Moves",
                                              "Enter the number of moves (5 "
                                              "- 200):"))
    return moves


def main():
    try:
        board_layout = BoardLayout()
        board_layout.window_setup()
        board_layout.splash_screen()

        puzzle_click = PuzzleClicks(player_name(), player_moves())
        leaderboard = Leaderboard()

        board_layout.run_graphics()
        leaderboard.read_leaderboard()
        leaderboard.sort_leaderboard()
        leaderboard.draw_leaderboard()

        puzzle_click.moves_number()
        puzzle_click.puzzle_thumbnail()
        puzzle_click.puzzle_pieces(puzzle_click.shuffle_numbers)
        puzzle_click.click_coordinates()

        turtle.done()

    except Exception as error:
        with open("5001_puzzle.err", mode="a") as outfile:
            outfile.write(f"An error happened - {error}\n")


if __name__ == '__main__':
    main()
