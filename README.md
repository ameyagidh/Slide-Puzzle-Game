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

## Screenshots:-

![Reset](https://user-images.githubusercontent.com/65457905/156274865-d5b567e0-b668-4ae4-9998-703abf665d6d.PNG)
![reset_luigi](https://user-images.githubusercontent.com/65457905/156274868-27e2229d-14ad-4995-8e5c-9c3f4ffdde90.PNG)
![reset_smiley](https://user-images.githubusercontent.com/65457905/156274869-c3541820-a8d2-48d9-9028-3c5736896439.PNG)
![Smiley](https://user-images.githubusercontent.com/65457905/156274871-d3e6546e-7415-4e83-9517-879f612f7a37.PNG)
![Splash](https://user-images.githubusercontent.com/65457905/156274872-f5d6cf61-8dfc-4ac9-98be-60484f73009a.PNG)
![winner](https://user-images.githubusercontent.com/65457905/156274873-ae2609f2-fa67-4d5f-97f4-5f8fe93646d9.PNG)
![errors](https://user-images.githubusercontent.com/65457905/156274874-27a32a72-0692-4984-a260-7e83b8c9da3b.PNG)
![Mario](https://user-images.githubusercontent.com/65457905/156274876-1bd9eab3-5f90-4211-af9e-1b0e0eb613ec.PNG)

