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
git clone https://github.com/ameyagidh/Slide-Puzzle-Game.git](https://github.com/ameyagidh/Slide-Puzzle-Game.git)
or download the zip file and run Main.py

### Requirements:-

 1. Python (Version 3.7 and higher)
 2. Python integrated development environment (IDE) preffered(Pycharm).

## Screenshots:-

<img width="1496" alt="Screenshot 2024-02-22 at 3 51 40 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/9532bb27-b9d7-4992-bdec-91f40336e25b">
<img width="797" alt="Screenshot 2024-02-22 at 3 52 02 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/fc83ab86-a2aa-4820-be46-49dd3a3f1f68">
<img width="792" alt="Screenshot 2024-02-22 at 3 52 22 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/8822bee0-38c3-43ec-acc1-c7b1ed945656">
<img width="790" alt="Screenshot 2024-02-22 at 3 52 54 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/222dec60-a32f-4ba2-8381-0292b3f9270c">
<img width="789" alt="Screenshot 2024-02-22 at 3 54 15 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/c4ed6255-23b4-4275-a2c6-7686515f9140">
<img width="794" alt="Screenshot 2024-02-22 at 3 53 52 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/13fc877c-2184-47b0-8716-96d0dfd151c5">
<img width="796" alt="Screenshot 2024-02-22 at 3 53 25 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/9d499ec0-af99-4b46-a5a9-883aadb4e532">
<img width="797" alt="Screenshot 2024-02-22 at 3 52 39 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/2874eb13-acb9-4d07-921f-fcf0e25f987f">
<img width="800" alt="Screenshot 2024-02-22 at 3 54 48 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/3435b56e-c395-4098-b529-5c68822ab7a8">
<img width="795" alt="Screenshot 2024-02-22 at 3 55 48 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/6c8f81a6-9c5e-4a41-9105-59043c87b41c">
<img width="794" alt="Screenshot 2024-02-22 at 3 56 43 AM" src="https://github.com/ameyagidh/Slide-Puzzle-Game/assets/65457905/3d375c13-b157-4572-9720-4cd0c4eb40cd">

