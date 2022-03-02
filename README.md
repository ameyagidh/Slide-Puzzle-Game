# Slide - Puzzle Game

Start the game 
Load a splash screen which has the splash image present in the resources file
I wanted a plain whit background for the puzzle hence included a1.gif file

After 3 seconds time (using the time library) the screen is changed and the user is prompted to 
add his name and moves [5 to 200]
error messages if any are written here or a message is printed to the screen

The Board is drawn, player moves and leaders are plotted using the turtle library
The Quit, Reset and Load images are added and the coordinates of these images are mapped
to the conditions in get_click function which acts according to the input (x,y) values

The default file loaded is mario.Images are plotted as objects of class images on the screen
with each image having the image name and coordinates as attributes.
 
These objects are appended to a list and when an object is clicked and it
matches the is_neighbour function the image is swapped with the blank image and 
these chnages are reflected in the list as well.

The images can be moved within the board play area. If the user finishes the game within 
the number of moves available then the player wins else the player has lost 

The player can choose from the load files resent if the file is not present then 
it results in reprompting the user for the right file name.

The player can use Quit button anytime to exit the game

The Reset button is a cheat which enables the user to get the puzzle to the right formation and thus help win win the game

There is a 5001_puzzle_err.txt file for appending the errors encountered during execution of the program
## Installation
Install my-project 

### Requirements:-

 1. Python (Version 3.7 and higher)
 2. Python integrated development environment (IDE) preffered(Pycharm).
 3. Unzip the file "fall_2021_final_project".
 4. Run the file puzzle_game.py.

Screenshots:-

    
