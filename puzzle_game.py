'''
Ameya Santosh Gidh
CS 5001, Fall 2021
Final Project - Puzzle Game
'''
import turtle
import os
import time
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CURRENTDIR = os.getcwd()

game_state = True
puz_name = ""

# Register image files
# Buttons
turtle.register_shape(CURRENTDIR+"\\Resources\\resetbutton.gif")
turtle.register_shape(CURRENTDIR+"\\Resources\\loadbutton.gif")
turtle.register_shape(CURRENTDIR+"\\Resources\\quitbutton.gif")

class Tile:
    """ Class: Tiles -> image(.gif) placed as tiles
        Attributes: Turtle, name, x, y, image, object(blank tile)
        Methods: str -> creates a human readable name for object
                    getters -> get_x, get_y (int) -> to get coordinates
                    setters -> set_x, set_y (int) -> to set coordinates
                    click -> move if adjacent
                    is_adjacent -> checks to see if tile is adjacent to
                                    blank tile
    """
    def __init__(self, name, x, y, image, other):
        """ Constructor - initializes instance of Tiles
            Param: name, coordinates(x, y), image-filepath
            Return: none
        """
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.shape(image)
        self.turtle.onclick(self.click)
        
        self.name = name
        self.x = x
        self.y = y
        self.image = image
        self.other = other

    def __str__(self):
        """ Method - converts object to human readable str
            Param: self
            Return: name of object
        """
        return self.name

    # Getters and setters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_val):
        self.x = new_val

    def set_y(self, new_val):
        self.y = new_val
    
    def click(self, x, y):
        """ Method - when clicked do something
            Param: self
                    x coordinate (int)
                    y coordinate (int)
            Return: do an event when object is clicked
        """
        # set variables
        my_x = self.x
        my_y = self.y
        blank_x = self.other.get_x()
        blank_y = self.other.get_y()

        # check if adjacent
        if self.is_adjacent(self.other):

            # if adjacent then swap
            self.x = blank_x
            self.y = blank_y
            self.turtle.goto(blank_x, blank_y)

            self.other.set_x(my_x)
            self.other.set_y(my_y)
            self.other.turtle.goto(my_x, my_y)

            # if tiles moved call funtion to add moves
            add_moves()
            
            player_score.set_text(moves)
            player_score.draw_text()

    def is_adjacent(self, other):
        """ Method - is_adjacent -> checks if adjacent to blank tile
            Param: self, other(blank tile)
            Return: bool(true if adjacent, false otherwise)
        """
        # set variables
        my_x = self.x
        my_y = self.y
        blank_x = other.x
        blank_y = other.y
        
        # check if adjacent and return true or false
        if ((((blank_x - 100) <= my_x <= (blank_x + 100))
             and (my_y == blank_y))
            or (((blank_y - 100) <= my_y <= (blank_y + 100))
                and (my_x == blank_x))):
            return True
        else:
            return False

class Button:
    """ Class: Buttons -> image(.gif) placed as Buttons
        Attributes: Turtle, name, x, y, image(file path)
        Methods: str -> creates a human readable name for object
                    click -> do something depending on the button
    """
    def __init__(self, name, x, y, image):
        """ Constructor - initializes instance of Buttons
            Param: name, coordinates(x, y), image-filepath
            Return: none
        """
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.shape(image)
        self.turtle.onclick(self.click)
        
        self.name = name

    def __str__(self):
        """ Method - converts object to human readable str
            Param: self
            Return: name of object
        """
        return self.name
    
    def click(self, x, y):
        """ Method - when clicked do something
            Param: self
            Return: do an event when object is clicked
        """
        print(self.name, x, y)
        # Load button condition
        if self.name == "Load Button":
            puzzle_name = turtle.textinput("Load Puzzle",
                                           "Enter the name of the puzzle"\
                                           + "you want to load.\n" +
                                           "Choices are:\n" + "mario.puz\n"
                                           + "luigi.puz\n" + "yoshi.puz\n"
                                           + "smiley.puz\n" + "fifteen.puz\n")
            if puzzle_name:
                load(puzzle_name)
            else:
                print("CANCELLED")
        # Quit button conditon
        elif self.name == "Quit Button":
            quit_game()
        # Reset button condition
        elif self.name == "Reset Button":
            global moves
            moves = 0
            
            tile_loop(path_dict, correct_coord_list)            
            
            player_score.set_text(moves)
            player_score.draw_text()

class ScreenText:
    """ Class: Buttons -> image(.gif) placed as Buttons
        Attributes:
        Methods:
    """
    def __init__(self, text, x, y, color, font, font_size, font_type):
        """ Constructor - initializes instance of Buttons
            Param: name, coordinates(x, y),
                    color, font, font_size(int),
                    font_type('normal', 'italic', 'bold')
            Return: none
        """
        self.turtle = turtle.Turtle()
        
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.font_size = font_size
        self.font_type = font_type

        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        
    def draw_text(self):
        """ Function - draw on screen texts on the console
            Param: text -> str -> collection of texts
                    x, y -> int -> coordinates
                    font(str)
                    font_size(int)
                    font_type(str) -> normal, bold, italics
            Return: none
        """
        # Draw text
        self.turtle.clear()
        self.turtle.write(self.text, False, align='left',
                          font=(self.font, self.font_size, self.font_type))

    def get_text(self):
        return self.text

    def set_text(self, new_val):
        self.text = "Player Moves:     " + str(moves)

def draw_border(x, y, move_x, move_y, color):
    """ Function - draw border
        Param: x, y -> int -> coordinates of starting point
                move_x, move_y -> int -> movement through x and y axis
                color -> color of border
        Return: none
    """
    # Initialize border settings
    border_pen = turtle.Turtle()
    border_pen.hideturtle()
    border_pen.speed(0)
    border_pen.color(color)
    border_pen.pensize(5)
    border_pen.penup()
    border_pen.setposition(x, y)
    border_pen.pendown()
    
    # Draw border
    border_pen.forward(move_x)
    border_pen.left(90)
    border_pen.forward(move_y)
    border_pen.left(90)
    border_pen.forward(move_x)
    border_pen.left(90)
    border_pen.forward(move_y)

def draw_text(text, x, y, color, font, font_size, font_type):
    """ Function - draw on screen texts on the console
        Param: text -> str -> collection of texts
                x, y -> int -> coordinates
                font(str)
                font_size(int)
                font_type(str) -> normal, bold, italics
        Return: none
    """
    # Initialize text settings
    text_pen = turtle.Turtle()
    text_pen.hideturtle()
    text_pen.speed(0)
    text_pen.color(color)
    text_pen.penup()
    text_pen.setposition(x, y)

    # Draw text
    text_pen.clear()
    text_pen.write(text, False, align='left',
                      font=(font, font_size, font_type))

def read_file(puzzle):
    """ Function: read puz files
        Param: puzzle -> .puz file
        Return: dictionary -> content of puz file
    """
    puz_dictionary = {}
    
    try:
        # read file
        with open(puzzle, 'r') as puz:
            for each in puz:
                key, value = each.split()
                key = key.strip(":")
                puz_dictionary[key] = value
            return puz_dictionary
                
    except:
        print("An exception occured!")

def path_dictionary(num_of_tiles, puz_dict):
    """ Function: path_dictionary
        Param: num_of_tiles -> int
                puz_dict -> dictionary
        Return: dictionary of full file path based on user's directory and os
    """
    path_dict = {}
    # iterating dictionary keys
    for i in range(num_of_tiles):
        num = str(i + 1)
        path_name = "path" + num
        print(path_name)
        path_dict[path_name] = ""

    # path for tiles -> values, and connecting them to keys in the dictionary
    count = num_of_tiles
    for each in path_dict:
        path_dict[each] = os.path.join(CURRENTDIR, puz_dict[str(count)])
        path_dict[each] = os.path.normpath(path_dict[each])
        turtle.register_shape(path_dict[each])
        count -= 1
        
    return path_dict

def tile_loop(path_dict, coord_list):
    """ Function: tile_loop -> create tiles
        Param: path_dict -> dictionary
                coord_matrix -> list -> matrix of coordinates
        Return: tile_list -> list
    """
    tile_pen = turtle.Turtle()

    # set names of distinct tiles
    tile_list = []
    tile_num = 0
    for i in range(len(path_dict)):
        num = str(i + 1)
        tile_name = "tile" + num
        print(tile_name)
        tile_list.append(tile_name)
    print(tile_list)

    # get coordinates
    print(coord_list)
    
    # loop to generate each tile
    i = 0
    for each in path_dict:
        turtle.register_shape(path_dict[each])
        tile_list[i] = Tile("Tile " + str(i + 1),
                            coord_list[i][0], coord_list[i][1],
                            path_dict[each], tile_list[0])
        print(tile_list[i], type(tile_list[i]))
        i += 1

    return tile_list

def coordinates_matrix(num_of_tiles):
    """ Function: matrix -> representation of the puzzle
        Param: num_of_tiles -> int
        Return: coord_list, list of coordinates arranged
    """
    root = math.sqrt(num_of_tiles)
    print(root)
    
    if int(root) ** 2 == num_of_tiles:
        is_square = True
    else:
        is_square = False

    if not is_square:
        print("number of tiles is not a perfect square")
    elif is_square:
        # create list of range(n) -> n = number_of_tiles
        list1 = list(range(1, num_of_tiles + 1))

        # Starting coordinate
        # 4 x 4 grid
        if num_of_tiles == 16:
            starting_coordinate = (10, -10)
        elif num_of_tiles == 9:
            starting_coordinate = (-90, 90)
        elif num_of_tiles == 4:
            starting_coordinate = (-190, 190)

        # create matrix of coordinates
        coord_matrix = []
        for i in range(int(root)):
            coord_matrix.append([])

        # append numbers on the matrix
        i_start = 0
        move_x = -100
        move_y = 100
        y = starting_coordinate[1]
        for i in range(int(root)):
            x = starting_coordinate[0]
            for each in list1[i_start : i_start + int(root)]:
                coordinates = (x, y)
                coord_matrix[i].append(coordinates)
                i_start += 1
                x += move_x
            y += move_y

        # reverse and print matrix
        coord_matrix.reverse()
        for i in range(len(coord_matrix)):
            coord_matrix[i].reverse()
            print(coord_matrix[i])
            
        # create list with 1 level and arranged
        coord_list = []
        for i in range(len(coord_matrix) - 1, -1, -1):
            for j in range(len(coord_matrix) - 1, -1, -1):
                coordinates = coord_matrix[i][j]
                coord_list.append(coordinates)
            
        return coord_list    

def read_leaders():
    """ Function: read puz files
        Param: none
        Return: none
    """
    text = ""
    try:
        # read file
       with open('leaderboard.txt', 'r') as rank:
           text = rank.readlines()[0:10]
           text = "\n".join(text)
                
    except:
        print("An exception occured!")

    return text

def swap(blank_pos, my_pos, blank_name, my_name):
    """ Function - swap
        Param: blank_pos
                my_pos
                blank_name
                my_name
        Return: none
    """
    print(blank_pos, my_pos, blank_name)

    blank_i = 0
    for i in range(len(tile_list)):
        name = tile_list[i].get_name()
        if name == blank_name:
            blank_i = i
        print(name, blank_name, blank_i)

    print(tile_list[blank_i])
    print(type(tile_list[blank_i]))

    tile_list[blank_i](blank_name, my_pos[0], my_pos[1], )

    Tile("Tile " + str(i + 1),
                            coord_list[i][0], coord_list[i][1],
                            path_dict[each], tile_list[0])

##    tile_list[blank_i]
##    tile_list[my_i]

def add_moves():
    """ Function add_moves
        Param: none
        Return: none
    """
    global moves
    moves += 1
    print(moves)

def on_close():
    """ Function - on_close -> when closing windows
        Param: none
        Return: none
    """
    exit()

def quit_game():
    """ Function - quit -> when pressing quit button
        Param: none
        Return: none
    """
    global game_state
    game_state = False
    print(game_state)
    return game_state

def load(puz_name="mario.puz"):
    """ Function - load -> new .puz file
        Param: none
        Return: none
    """
    global moves, path_dict, correct_coord_list, shuffled_coord_list
    moves = 0

    # clear
    wn = turtle.Screen()
    wn.clearscreen()

    # Draw puzzle border
    draw_border(-360, -130, 480, 480, 'black')

    # Draw leader board border
    draw_border(150, -130, 200, 480, 'blue')
    
    # Draw game options board
    draw_border(-360, -310, 710, 120, 'black')

    # Read leaderboard file
    leaders_txt = read_leaders()
    print(leaders_txt)

    # Leader board variables
    lb_header = "Leaders:"
##    lb_list = leaders_txt

    # Leader board header
    draw_text(lb_header, 160, 310, 'blue', 'Arial', 16, 'normal')

    # Leading players
    draw_text(leaders_txt, 170, -80, 'blue', 'Arial', 12, 'normal')

##    # Player move options - text
##    draw_text("Player Moves:     " + str(moves), -320, -275, 'black',
##              'Arial', 22, 'bold')

    # create buttons
    # reset button
    reset_button_pen = turtle.Turtle()
    reset_button = Button("Reset Button", 80, -250,
                         CURRENTDIR+"\\Resources\\resetbutton.gif")
    print(reset_button)

    # load button
    load_button_pen = turtle.Turtle()
    load_button = Button("Load Button", 180, -250,
                         CURRENTDIR+"\\Resources\\loadbutton.gif")
    print(load_button)

    # quit button
    quit_button_pen = turtle.Turtle()
    quit_button = Button("Quit Button", 280, -250,
                         CURRENTDIR+"\\Resources\\quitbutton.gif")
    print(quit_button)

    # create dictionary from puz file loaded
    puz_dict = read_file(puz_name)
    print(puz_dict)
    grid_size = int(puz_dict['number'])
    print(grid_size)

    # path for puz file
    puz_name = puz_dict['name'] + ".puz"
    print()
    print(puz_name)
    print()
    theme_path = os.path.join(CURRENTDIR, puz_name)
    theme_path = os.path.normpath(theme_path)

    print()
    print(theme_path)
    print()
    
    thumbnail_name = puz_dict['thumbnail']
    thumbnail_path = os.path.join(CURRENTDIR, puz_dict['thumbnail'])
    thumbnail_path = os.path.normpath(thumbnail_path)

    print()
    print(thumbnail_path)
    print()

    # create thumbnail from gif images
    thumbnail_pen = turtle.Turtle()
    thumbnail_pen.penup()
    thumbnail_pen.speed(0)
    thumbnail_pen.setposition(320, 320)
    turtle.register_shape(thumbnail_path)
    thumbnail_pen.shape(thumbnail_path)

    # create coordinate matrix
    correct_coord_list = coordinates_matrix(grid_size)
    print(correct_coord_list)

    # create copy of correct coordinates then shuffle
    shuffled_coord_list = correct_coord_list.copy()
    random.shuffle(shuffled_coord_list)
    print(shuffled_coord_list)
    print()
    print()
    print(correct_coord_list == shuffled_coord_list)
    print()
    print()

    # create puzzle tiles
    num_of_tiles = grid_size
    path_dict = path_dictionary(num_of_tiles, puz_dict)
    print()
    print("PATH DICTIONARY", path_dict)
    print()

    # render tiles and get tile list
    tile_list = tile_loop(path_dict, shuffled_coord_list)

    return tile_list

def run_game():
    global moves, tile_list, player_score
    
    # input name
    player_name = turtle.textinput("CS5001 Puzzle Slide", "Your Name:")

    # input number of moves
    number_of_moves = turtle.numinput("CS5001 Puzzle Slide",
                                      "Enter the number of moves "
                                      + "(chances) you want (5-200)?",
                                      5, 5, 200)
    
    # Creating windows screen and initializing settings
    wn = turtle.Screen()
    wn.clearscreen()
    wn.bgcolor('white')
    wn.title("CS5001 Sliding Puzzle Game")
    wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    wn.tracer(0)

    # capture close event when closing window
    canvas = wn.getcanvas()
    root = canvas.winfo_toplevel()
    root.protocol("WM_DELETE_WINDOW", on_close)

    # load splash screen for 3 seconds
    wn.bgpic(CURRENTDIR+"\\Resources\\splash_screen.gif")
    wn.update()
    time.sleep(3)

    # clear splash screen
    wn.clear()
    wn.update()

    # load new puzzle
    tile_list = load()
    print()
    print(tile_list[0])
    print(tile_list[5])
    print(tile_list[7])

    # tile_list
    print("TILE LIST", tile_list)
    
    random.shuffle(tile_list)
    print(tile_list[1])

    # player score
    player_score_pen = turtle.Turtle()

    player_score = ScreenText("Player Moves:     " + str(moves),
                                      -320, -275,'black', 'Arial', 22, 'bold')
    player_score.draw_text()
    
    # Main loop
    while game_state == True:
        try:
            # Update the screen
            wn.update()
            
            # Clear screen

            # Do stuff
        
        except turtle.Terminator:
            # exception error when you close window while game is running
            quit()

    # clear screen
    wn.clear()
    wn.update()

    # load credits screen for 3 seconds then close
    wn.bgpic(CURRENTDIR+"\\Resources\\credits.gif")
    wn.update()
    time.sleep(3)
    wn.bye()
    raise SystemExit

if __name__ == "__main__":
    run_game()
