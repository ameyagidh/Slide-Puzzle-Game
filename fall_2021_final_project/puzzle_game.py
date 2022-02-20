import turtle
import time
from turtle import Screen, Turtle
import os
import random
import datetime
from datetime import date
import calendar
today = date.today()
day = calendar.day_name[date.today().weekday()]
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
path = os.getcwd()
lst_luigi = [[-240, 240], [-140, 240], [-40, 240], [-240, 140], [-140, 140], [-40, 140], [-240, 40], [-140, 40], [-40, 40]]
lst_yoshi = [[-240, 240], [-140, 240], [-240, 140], [-140, 140]]
lst_default = [[-240, 240], [-140, 240], [-40, 240], [60, 240], [-240, 140], [-140, 140], [-40, 140], [60, 140], [-240, 40], [-140, 40], [-40, 40], [60, 40], [-240, -60], [-140, -60], [-40, -60], [60, -60]]
# lst for plotting the square tiles on the screen

lst_winner_16 = [['16.gif', [-240, 240]], ['15.gif', [-140, 240]], ['14.gif', [-40, 240]], ['13.gif', [60, 240]],
                        ['12.gif', [-240, 140]], ['11.gif', [-140, 140]], ['10.gif', [-40, 140]],
                        ['9.gif', [60, 140]], ['8.gif', [-240, 40]], ['7.gif', [-140, 40]], ['6.gif', [-40, 40]],
                        ['5.gif', [60, 40]], ['4.gif', [-240, -60]], ['3.gif', [-140, -60]], ['2.gif', [-40, -60]],
                        ['blank.gif', [60, -60]]]

win_16 = ["16.gif","15.gif","14.gif","13.gif","12.gif","11.gif","10.gif","9.gif","8.gif",
          "7.gif","6.gif","5.gif","4.gif","3.gif","2.gif","blank.gif"]
# win_16 has the required image order for a 4 X 4 puzzle
win_9 = ["9.gif","8.gif","7.gif","6.gif","5.gif","4.gif","3.gif","2.gif","blank.gif"]
# win_9 has the required image order for a 4 X 4 puzzle
win_4 = ["4.gif","3.gif","2.gif","blank.gif"]
# win_5 has the required image order for a 4 X 4 puzzle

lst_winner_9 = [["9.gif", [-240, 240]],["8.gif", [-140, 240]],["7.gif", [-40, 240]],
                    ["6.gif" ,[-240, 140]],["5.gif" ,[-140, 140]],["4.gif" ,[-40, 140]],
                    ["3.gif" ,[-240, 40]],["2.gif" ,[-140, 40]],["blank.gif", [-40, 40]]]

lst_winner_4 = [["4.gif", [-240, 240]],["3.gif", [-140, 240]],["2.gif" ,[-240, 140]],["blank.gif", [-140, 140]]]

# lst_winner_16, lst_winner_9, lst_winner_4 is used to get the the right image positions
# turtle initialization on the screen
t0 = turtle.Turtle()
t0.hideturtle()
t0.speed(0)
# speedup the turtle
wn = turtle.Screen()
wn.title("Puzzle Game")
# Title for the turtle game screen
width = 700
# width of the screen
height = 700
# height of the screen
leader = "leaders.txt"
# file which stores the leaders
wn.setup(width,height)
blank = {}

moves = 100
moves_save = 100

t00 = turtle.Turtle()
name = ""
# name variable contains the player name which is set to 0 as default

screen = Screen()
n = 16
'''
n is the number of images in the puzzle and as the game starts with mario 
default value of n is 6
'''
file_name = "mario"

lst = []
# lst is used to store all coordinates of the objects

lst21 = []
# lst2 has objects of 9 X 9 puzzle

lst2 = []
# lst2 has objects of 16 X 16 puzzle

lst23 = []
# lst23 has the objects of 4 X 4 puzzle

# Empty lists are declared for storing the image objects
r = 0
t2 = turtle.Turtle()
x = 1
# x is a counter for checking if a file is valid

def Start_screen():
    '''
    Start_screen function is used to start the game
    with a splash screen
    '''
    wn.bgpic("Resources\splash_screen.gif")
    # Adding a background image
    t00.hideturtle()
    wn.listen()
    time.sleep(2)
def input_screen():
    '''
    Runs the turtle game
    within the function name (of the player)
    and the moves the player
    needs to unscramble the puzzle
    are taken as input
    '''
    global name
    game_state = "run_game"
    if game_state == "run_game":
        turtle.bgpic("a1.gif")
    name = str(turtle.textinput("CS5001 puzzle game", "Your name"))
    # name of the player is stored in the variable name
    if name == "":
        name = "guest"
    game_state = "moves"
    if game_state == "moves":
        turtle.bgpic("a1.gif")
    Moves = turtle.textinput("Enter the number of moves(chances) you want (5,200)?", "Moves")
    # moves variable takes the number of moves the player needs to unscramble the puzzle as the input

    # checking the condition for the input if the number of moves is int and between 5 to 200
    # if condition is met then the program continues else the program shows error message

    try:
        if (isinstance(int(Moves), int)):
            if (int(Moves) >= 5 and int(Moves) <= 200):
                global moves
                moves = int(Moves)
                global moves_save
                moves_save = int(Moves)
                winner_flag = 0
                return winner_flag, moves
            else:
                with open("5001_puzzle_err.txt", mode="a+") as error_file:
                    error_file.write(str(day) + " " + str(now.strftime("%d-%B")) + " " +
                                     str(current_time) + " " + str(today.year) + " ")
                    error_file.write("Error: moves not in range ")
                    error_file.write(" " + "LOCATION: " + "input_screen()\n")
    except:
        with open("5001_puzzle_err.txt", mode="a+") as error_file:
            error_file.write(str(day) + " " + str(now.strftime("%d-%B")) + " " +
                             str(current_time) + " " + str(today.year)  + " ")
            error_file.write("Error Enter an integer value" )
            error_file.write(" " + "LOCATION: " + "input_screen()\n")
            time.sleep(2)
            turtle.bye()
def load_file(file_name_puz="mario.puz"):
    file_name = file_name_puz.split(".")[0]
    with open(file_name_puz, mode="r") as data:
        for line in data:
            if line.startswith("number"):
                number = int(line.split(":")[-1].strip("\n"))
            elif line.startswith("name"):
                name = line.split(":")[-1].strip("\n")
                name = name.split("_")[0]
            elif line.startswith("size"):
                size = int(line.split(":")[-1].strip("\n"))
    sqrt = size ** 0.5
    valid = [4, 9, 16]
    if (sqrt not in valid or size not in range(50, 110) or
            name == "malformed"):
        with open("5001_puzzle_err.txt", mode="a+") as error_file:
            error_file.write(str(day) + " " + str(now.strftime("%d-%B")) + " " +
                             str(current_time) + " " + str(today.year) + " ")
            error_file.write("Error: malformed data")
            error_file.write(" " + "LOCATION: "+ "load_file()\n")
    file_name_dict = {file_name_puz: int(number)}
    factors = []
    # factors variable will contain the rows and columns
    lst_cordinates = []
    # lst_cordinates is an empty list which will
    # have the cordinates of the board
    for row in range(sqrt):
        for column in range(sqrt):
            lst.append([])
    x_old = -240
    x = -240
    y = 240
    j = 0
    for i in range(len(lst)):
        if i % sqrt == 0 and i > 0:
            x = x_old
            y = y - size
        lst_cordinates[i].append(x)
        lst_cordinates[i].append(y)
        x = x + size
    return lst, number , file_name_dict
def draw_board():
    '''
    Function draw_board is used to make
    the game board
    '''
    # Drawing top square
    t0.penup()
    t0.setx(-(width/2) + 50)
    t0.sety((height/2) - 50)
    t0.pendown()
    t0.forward(420)
    t0.right(90)
    t0.forward(height - 250)
    t0.right(90)
    t0.forward(420)
    t0.right(90)
    t0.forward(height - 250)
    t0.right(90)

    # Drawing below square
    t0.penup()
    t0.setx(-(width / 2) + 50)
    t0.sety(-200)
    t0.pendown()
    t0.forward(width - 100)
    t0.right(90)
    t0.forward(90)
    t0.right(90)
    t0.forward(width - 100)
    t0.right(90)
    t0.forward(90)
    t0.right(90)

    # Drawing right side square
    t0.penup()
    t0.setx(130)
    t0.sety((height / 2) - 50)
    t0.pendown()
    t0.pencolor("Blue")
    t0.forward(160)
    t0.right(90)
    t0.forward(450)
    t0.right(90)
    t0.forward(160)
    t0.right(90)
    t0.forward(450)
    t0.right(90)
    t0.pencolor("Black")
def Tools(x, y, image):
    '''
    Tools function takes
    :param x:
    :param y:
    :param image:
    :output plots the image on the screen
    '''
    t = Turtle()
    t.speed(0)
    t.shape(image)
    t.penup()
    t.goto(x, y)
def files_presents():
    """
    Function files_present finds all the files ending with .puz
    and appends them to a list
    :return: files_present which is a list of all the .puz files
    """
    files_present = []
    files_present1 = []
    for file in os.listdir(path):
        if file.endswith(".puz"):
            files_present1.append(os.path.join(file))
            files_present.append(os.path.join(file+"\n"))
    if len(files_present) > 10:
        file_warning = r"Resources\\file_warning.gif"
        screen = Screen()
        screen.addshape(file_warning)
        Tools(-60, 70, file_warning)
    return files_present,files_present1
def image():
    '''
    image function plots the buttons
    on the screen which are the load
    reset and quit
    '''

    # defining the button images
    Quit_button = r"Resources\\quitbutton.gif"
    Load_button = r"Resources\\loadbutton.gif"
    Reset_button = r"Resources\\resetbutton.gif"
    screen2 = Screen()
    screen2.addshape(Quit_button)
    Tools(240, -250, Quit_button)
    screen2 = Screen()
    screen2.addshape(Load_button)
    Tools(150, -250, Load_button)
    screen2 = Screen()
    screen2.addshape(Reset_button)
    Tools(60, -250, Reset_button)
def load_button():
    '''
    The load_button is used when the load button
    is pressed if the file is present the the earlier puzzle is
    cleared and replaced by a new puzzle which the user selects
    else it gives an error message on the screen
    '''

    files_present,files_present1 = files_presents()
    a = "".join(files_present)
    for i in range(len(files_present)):
        files_present[i] = files_present[i].split('.')[0]
    # file_name denotes the file name currently being used
    global file_name
    global x
    global n
    file_name = turtle.textinput("Enter the name of the puzzle you want to load "
                                 "your choices are",a)
    file_name = file_name.split(".")[0]
    file_name1 = file_name
    if file_name.lower() in files_present:
        if file_name == "yoshi":
            # l1 = lst_yoshi
            global n
            n = 4
        elif file_name == "luigi":
            n = 9
        elif file_name == "mario" or file_name == "smiley" or file_name == "fifteen":
            n = 16
        elif file_name.startswith("malformed_"):
            error_img = r"Resources\\file_error.gif"
            sc = Screen()
            sc.addshape(error_img)
            Tools(-60, 70, error_img)
            x = 0
            # x  is used to check if the file is malformed or not
        if x != 0:
            file_name = "blank"
            fill_puzzle_obj_blank()
            file_name = file_name1
            global lst2
            lst2 = []
            global lst21
            lst21 = []
            global moves
            moves = moves_save
            t2.clear()
            t2.write(moves, font="bold")

            if n == 9:
                fill_puzzle_obj2(r = 0)
            elif n == 4:
                fill_puzzle_obj3(r = 0)
            else:
                fill_puzzle_obj(r = 0)
    else:
        error_img = r"Resources\\file_error.gif"
        sc = Screen()
        sc.addshape(error_img)
        Tools(-60, 70, error_img)
def write_fn(moves,winner_flag = 0):
    '''
    :param moves:
    :param winner_flag: set to zero at the start
    write_fn function writes the leaders on the leaderboard
    and if the player wins even his name is written
    using the winner flag which iis changed if the player wins
    '''
    if winner_flag == 0:
        turtle.penup()
        turtle.setx(-250)
        turtle.sety(-250)
        turtle.pendown()
        turtle.write("Players Moves: ", font="bold")
        turtle.penup()
        t2.penup()
        t2.setx(-110)
        t2.sety(-250)
        t2.write(moves, font="bold")
        turtle.setx(130)
        turtle.sety(240)
        turtle.pendown()
        turtle.pencolor("Blue")
        turtle.write("Leaders", font="bold")
        turtle.penup()
        turtle.setx(130)
        alpha = 190
        turtle.sety(alpha)
        turtle.pendown()
        try:
            with open(leader, "r") as leaders:
                for x in leaders:
                    turtle.write(x, font="bold")
                    turtle.penup()
                    alpha = alpha - 30
                    turtle.sety(alpha)
                    turtle.pendown()
            turtle.pencolor("Black")
        except:
            leaderboard_error = r"Resources\\leaderboard_error.gif"
            sc = Screen()
            sc.addshape(leaderboard_error)
            Tools(-60, 70, leaderboard_error)
    # else case when the player solves the puzzle successfully
    else:
        try:
            with open("leaders.txt", "a") as leaders:
                leaders.write("\n"+name)
        except:
            leaderboard_error = r"Resources\\leaderboard_error.gif"
            sc = Screen()
            sc.addshape(leaderboard_error)
            Tools(-60, 70, leaderboard_error)

def fill_puzzle_thumbnail(image_dir,lst1):
    '''
    fill_puzzle_thumbnail takes inout as
    :param image_dir: which image to be plotted
    :param lst1: contains the coordinates of the image to be plotted
    '''
    # x and y are the x and y coordinates of the image
    x = lst1[0]
    y = lst1[1]
    t0 = turtle.Turtle()
    t0.speed(0)
    t0.shape(image_dir)
    t0.penup()
    t0.goto(x, y)
class images_class:
    '''
    image_class is the class which
    has image objects which have image_name and cordinates as attributes
    '''

    def __init__(self,image_name,cord):
        self.image_name = image_name
        # image_name is the image name of the file
        self.cord = cord
        # cord contains the coordinates of the image to be plotted
    def fill_puzzle(self,i, lst1, c= 0):
        ''''
        fill_puzzle is used to fill the images on the turtle screen here the
        list and counter c for the blank image placement is taken as input
        '''
        if c == 1:
            image_dir = r"Images\\" + file_name + "\\blank.gif"
        else:
            image_dir = r"Images\\" + file_name + "\\" + str(i) + ".gif"
        # x and y are the x and y coordintes of the image
        x = lst1[0]
        y = lst1[1]
        t0 = turtle.Turtle()
        t0.speed(0)
        t0.shape(image_dir)
        t0.penup()
        t0.goto(x, y)
    def fill_puzzle2(self,image_dir,x_y):
        x = x_y[0]
        y = x_y[1]
        t0 = turtle.Turtle()
        t0.speed(0)
        t0.shape(image_dir)
        t0.penup()
        t0.goto(x,y)
    def thumb_nail(self,file_name, c=0):
        '''
        thumb_nail function is used to plot the thumb nail image on the screen
        :param file_name:
        :param c:
        :return:
        '''
        t_thumb_sc = turtle.Screen()
        if c == 0:
            image_thumbnail = r"Images\\" + file_name + "\\" + file_name + "_thumbnail.gif"
            t_thumb_sc.addshape(image_thumbnail)
            fill_puzzle_thumbnail(image_thumbnail, [280, 240])
        else:
            image_thumbnail = r"Images\\" + file_name + "\\blank.gif"
            t_thumb_sc.addshape(image_thumbnail)
            fill_puzzle_thumbnail(image_thumbnail, [280, 240])
    def plot(self,i, c= 0):
        '''
        plot is used to plot images in the jumbled order
        :param self:
        :param i:
        :param c:
        :return:
        '''
        if file_name == "luigi":
            lst = lst_luigi[::]
        elif file_name == "yoshi":
            lst = lst_yoshi[::]
        else:
            lst = lst_default[::]
        if c == 1 :
            image_dir = r"Images\\" + file_name + "\\blank.gif"
            wn.addshape(image_dir)
            self.fill_puzzle(i, lst[i - 1], c = 1)
        else:
            image_dir = r"Images\\" + file_name + "\\" + str(i) + ".gif"
            wn.addshape(image_dir)
            self.fill_puzzle(i, lst[i-1])
        if i == n - 1:
             self.thumb_nail(file_name)
    def plot2(self):
        '''
        plot is used to plot images in the jumbled order
        :param self:
        :param i:
        :param c:
        :return:
        '''
        if file_name == "luigi":
            lst = lst_luigi[::]
        elif file_name == "yoshi":
            lst = lst_yoshi[::]
        else:
            lst = lst_default[::]
        image_dir = r"Images\\"+ file_name +"\\"+ self.image_name
        wn.addshape(image_dir)
        self.fill_puzzle2(image_dir,self.cord)
        self.thumb_nail(file_name)
    def img_swap(self,other):
        '''
        img_wap takes 2 image_classs objects if they
        are neighbours then they are swapped
        :param self:
        :param other:
        :return:
        '''

        # temp1 and temp2 are used to swap the images
        temp1 = self.cord[0]
        temp2 = self.cord[1]

        self.cord[0] = other.cord[0]
        self.cord[1] = other.cord[1]

        other.cord[0] = temp1
        other.cord[1] = temp2

        image_dir = r"Images\\" + file_name + "\\" + self.image_name.split(".")[0] + ".gif"
        wn.addshape(image_dir)
        self.fill_puzzle(self.image_name.split(".")[0], self.cord)
    def is_a_neighbour(self, other):
        '''
        is_a_neighbour checks if the two images are neighbours
        of each other if yes it returns true else it returns false
        :param self:
        :param other:
        '''
        if (self.cord[0] == other.cord[0] + 100 and self.cord[1] == other.cord[1]):
            return True
        elif (self.cord[0] == other.cord[0] - 100 and self.cord[1] == other.cord[1]):
            return True
        elif (self.cord[1] == other.cord[1] + 100 and self.cord[0] == other.cord[0]):
            return True
        elif (self.cord[1] == other.cord[1] - 100 and self.cord[0] == other.cord[0]):
            return True
        else:
            return False
def wn_fn():
    # wn_fn is used to add the winner message to the screen
    winner_image = r"Resources\\winner.gif"
    sc = Screen()
    sc.addshape(winner_image)
    Tools(-60, 70, winner_image)
    write_fn(moves,winner_flag=1)
    time.sleep(3)
    turtle.bye()
def lose_fn():
    # lose_fn is used to add the winner message to the screen
    lose_image = r"Resources\\Lose.gif"
    sc = Screen()
    sc.addshape(lose_image)
    Tools(-60, 70, lose_image)
    time.sleep(3)
    turtle.bye()
def get_click(x, y):
    '''
    function get_click takes input
    :param x:
    :param y:
    :works on the click which button and what to do on that click
    '''
    global moves
    global lst2
    # moves is used to decrement the moves variable

    if (x in range(205,280) and y in range(-270, -230)):
        quit_button()
    elif (x in range(110,180) and y in range(-280, -220)):
        load_button()
    elif (x in range(25,100) and y in range(-295, -212)):
        Reset_button()
    else:
        if n==9:
            for i in range(n):
                if (x in range(lst21[i].cord[0] - 60, lst21[i].cord[0] + 60)
                    and y in range(lst21[i].cord[1] - 60, lst21[i].cord[1] + 60)):
                        if lst21[i].is_a_neighbour(lst21[n-1]):
                            lst21[i].img_swap(lst21[n-1])
                            moves = moves - 1
                            t2.clear()
                            t2.write(moves, font="bold")
                            counter = 0
                            # counter is to check the winner
                            for i in range(len(lst21)):
                                if lst21[i].image_name == win_9[i]:
                                    counter = counter + 1
                            if counter == len(win_9):
                                wn_fn()
                        if moves == 0:
                            lose_fn()
        elif n==4:
            for i in range(n):
                if (x in range(lst23[i].cord[0] - 60, lst23[i].cord[0] + 60)
                    and y in range(lst23[i].cord[1] - 60, lst23[i].cord[1] + 60)):
                        if lst23[i].is_a_neighbour(lst23[n-1]):
                            lst23[i].img_swap(lst23[n-1])
                            moves = moves - 1
                            t2.clear()
                            t2.write(moves,font="bold")
                            counter = 0
                            # counter is to check the winner
                            for i in range(len(lst23)):
                                if lst23[i].image_name == win_4[i]:
                                    counter = counter + 1
                            if counter == len(win_4):
                                wn_fn()
                        if moves == 0:
                            lose_fn()
        else:
            for i in range(n):
                if (x in range(lst2[i].cord[0] - 60, lst2[i].cord[0] + 60)
                    and y in range(lst2[i].cord[1] - 60, lst2[i].cord[1] + 60)):
                    if lst2[i].is_a_neighbour(lst2[n-1]):
                        lst2[i].img_swap(lst2[n-1])
                        moves = moves - 1
                        t2.clear()
                        t2.write(moves,font="bold")
                        counter = 0
                        # counter is to check the winner
                        for i in range(len(lst2)):
                            if lst2[i].image_name == win_16[i]:
                                counter = counter + 1
                        print(counter)
                        if counter == len(win_16):
                            wn_fn()
                    if moves == 0:
                        lose_fn()
def Reset_button():
    '''
    Reset_button is used to reset the puzzle back to its
    original form
    '''
    global n
    global lst2
    global lst21
    global lst23
    lst2 = lst2.clear()
    lst2 = []
    lst21 = lst21.clear()
    lst21 = []
    lst23 = lst23.clear()
    lst23 = []
    if n == 16:
        fill_puzzle_obj(r=1)
    elif n == 9:
        fill_puzzle_obj2(r=1)
    elif n == 4:
        fill_puzzle_obj3(r=1)
def fill_puzzle_obj_blank():
    '''
    fill_puzzle_obj_blank is used to make the images as objects
    of class image for blank image
    :param file_name:
    :param r:
    :return:
    '''
    n = 16
    lst = lst_default
    file_name = "blank"
    for i in range(1,n+1):
        obj_name = "blank.gif"
        obj = images_class(obj_name, lst[i-1])
        obj.plot(i)
def fill_puzzle_obj(r=0):
    '''
    fill_puzzle_obj is used to make the images as objects
    of class image
    :param file_name:
    :param r:
    :return:
    '''
    n = 16
    lst = lst_default
    '''
    r is used to check the reset is triggered or not 
    r = 0 is not reset and r = 1 triggers the reset button
    '''
    global lst2
    if r == 0:
        for i in range(1, n+1):
            if (i == n):
              obj_name = "blank.gif"
              obj = images_class(obj_name, lst[i-1])
              obj.plot(i, c=1)

            else:
                obj_name = str(i) + ".gif"
                obj = images_class(obj_name, lst[i-1])
                obj.plot(i)
            lst2.append(obj)
        wn.onclick(get_click)
    elif r == 1:
        for i in range(len(lst_winner_16)):
            obj = images_class(lst_winner_16[i][0],lst_winner_16[i][1])
            obj.plot2()
            lst2.append(obj)
        wn.onclick(get_click)
def fill_puzzle_obj2(r=0):
    '''
    fill_puzzle_obj2 is used to make the images as objects
    of class image
    :param file_name:
    :param r:
    :return:
    '''
    n = 9
    lst = lst_luigi
    '''
    r is used to check the reset is triggered or not 
    r = 0 is not reset and r = 1 triggers the reset button
    '''
    global lst21
    if r == 0:
        for i in range(1, n + 1):
            if (i == n):
                obj_name = "blank.gif"
                obj = images_class(obj_name, lst[i - 1])
                obj.plot(i, c=1)

            else:
                obj_name = str(i) + ".gif"
                obj = images_class(obj_name, lst[i - 1])
                obj.plot(i)
            lst21.append(obj)
        wn.onclick(get_click)
    else:
        for i in range(len(lst_winner_9)):
            obj = images_class(lst_winner_9[i][0],lst_winner_9[i][1])
            obj.plot2()
            lst21.append(obj)
        wn.onclick(get_click)
def fill_puzzle_obj3(r=0):
    '''
    fill_puzzle_obj3 is used to make the images as objects
    of class image
    :param file_name:
    :param r:
    :return:
    '''
    n = 4
    lst = lst_yoshi
    '''
    r is used to check the reset is triggered or not 
    r = 0 is not reset and r = 1 triggers the reset button
    '''
    global lst23
    if r == 0:
        for i in range(1, n + 1):
            if (i == n):
                obj_name = "blank.gif"
                obj = images_class(obj_name, lst[i - 1])
                obj.plot(i, c=1)

            else:
                obj_name = str(i) + ".gif"
                obj = images_class(obj_name, lst[i - 1])
                obj.plot(i)
            lst23.append(obj)
        wn.onclick(get_click)
    else:
        for i in range(len(lst_winner_4)):
            obj = images_class(lst_winner_4[i][0],lst_winner_4[i][1])
            obj.plot2()
            lst23.append(obj)
        wn.onclick(get_click)
def quit_button():
    # quit_button function quits the game when it is clicked
    quit_image = r"Resources\\quitmsg.gif"
    screen = Screen()
    screen.addshape(quit_image)
    Tools(-60, 70, quit_image)
    time.sleep(3)
    turtle.bye()
def main():
    Start_screen()
    winner_flag, moves = input_screen()
    write_fn(moves, winner_flag)
    '''
    winner_flag variable is used to check if a player wins the game if it is 1 then
    players name is written to the leaderboard
    '''
    draw_board()
    image()
    fill_puzzle_obj()
    turtle.mainloop()
if __name__=="__main__":
    main()

