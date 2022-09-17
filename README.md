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
git clone https://github.com/ameyagidh/Slide-Puzzle-Game.git
or download the zip file then 
Unzip the file "fall_2021_final_project".
Run the file puzzle_game.py.

### Requirements:-

 1. Python (Version 3.7 and higher)
 2. Python integrated development environment (IDE) preffered(Pycharm).

## Screenshots:-

![Reset](https://user-images.githubusercontent.com/65457905/156275267-7960d039-b6be-4f16-b196-13fd4f043c74.PNG)
![reset_smiley (1)](https://user-images.githubusercontent.com/65457905/156275268-10bfb46b-292a-4a50-8977-751109c6f9ff.png)
![Smiley](https://user-images.githubusercontent.com/65457905/156275409-454dce9c-1a43-42fe-93d5-3c7d48313ed8.PNG)
![winner](https://user-images.githubusercontent.com/65457905/156275273-94f064db-9dc1-43b8-ba70-09666613e772.PNG)
![reset_luigi](https://user-images.githubusercontent.com/65457905/156275274-0fcfbe0a-ac4f-40a0-9e9f-5f0479765cfd.PNG)
![errors](https://user-images.githubusercontent.com/65457905/156275275-034371ba-8ca6-4ad8-9c2f-20c6155721c6.PNG)
![Mario](https://user-images.githubusercontent.com/65457905/156275277-72d8e8a1-08cd-4201-804b-085d3ddce703.PNG)
