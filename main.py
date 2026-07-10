'''
==========================================================
    Assignment#1 --> Student ID (2601143) 
==========================================================
'''
from graphix import *

ALLOW_COLOURS = ["red", "green", "blue", "purple", "magenta", "orange"]
ALLOW_SIZES = ["5","7","9","11","13"]

# GLOBAL variables for challenge part of code.
selected = None
selection_border = None
PATCH_SIZE = 100


patch_states = {} 


# USER INPUTS

def input_three_colour():
    first_colour = input_colour("Enter first colour: ")

    while True:
        second_colour = input_colour("Enter second colour: ")
        if second_colour != first_colour:
            break
        print("Choose a different colour.")

    while True:
        third_colour = input_colour("Enter third colour: ")
        if third_colour not in (first_colour, second_colour):
            break
        print("Choose a different colour.")

    return [first_colour, second_colour, third_colour]




def input_colour(user_given_colour):
    while True:
        colour = input(user_given_colour).strip().lower()
        if colour in ALLOW_COLOURS:
            return colour
        print("Selected colour is incorrect; Choose from ", ALLOW_COLOURS)


def input_size():
    while True:
        size = input("Enter the size of patch from [5,7,9,11,13]: ")
        if size in ALLOW_SIZES:
            return int(size)
        print("Selected size is incorrect: Choose from ", ALLOW_SIZES)


# PATCH DESIGN FUNCTIONS 

def draw_penultimate_patch(win, x, y, colour):
    patch_width = 100
    patch_height = 100
    
    cols = 5
    rows = 4
    
    cell_width = 20
    cell_height = 25
    
    # x and y point of one cell
    oval_x = 10  
    oval_y = 15
    
    # radius of circle of each cell
    circle_radius = 10
    
    for col in range(cols):
        for row in range(rows):
            circle_x = int(x + col * cell_width + (cell_width / 2))
            circle_y = int(y + row * cell_height + (cell_height /2))
            
            if col % 2 == 0:
                if row % 2 == 0: 
                    circle = Circle(Point(circle_x , circle_y - 2) , 10)
                    circle.fill_colour = colour
                    circle.outline_colour = colour
                    circle.outline_width = 0
                    circle.draw(win)
                else:
                    oval = Oval(
                        Point(int(circle_x - oval_x), int(circle_y - oval_y - 2)),
                        Point(int(circle_x + oval_x), int(circle_y + oval_y - 2))
                    )
                    oval.fill_colour = colour
                    oval.outline_colour = colour
                    oval.outline_width = 0
                    oval.draw(win)
            else:
                if row % 2 == 0:
                    oval = Oval(
                        Point(circle_x - oval_x, circle_y - oval_y + 3),
                        Point(circle_x + oval_x, circle_y + oval_y + 3)
                    )
                    oval.fill_colour = colour
                    oval.outline_colour = colour
                    oval.outline_width = 0
                    oval.draw(win)
                else:
                    circle = Circle(Point(circle_x , circle_y + 3) , circle_radius)
                    circle.fill_colour = colour
                    circle.outline_colour = colour
                    circle.outline_width = 0
                    circle.draw(win)


def draw_last_digit_patch(win, x, y, colour):
    each_stair_height = 10
    for step in range(10):
        x1 = x + step * each_stair_height  
        y1 = y + (100 - (step + 1) * each_stair_height)
        x2 = x1 + each_stair_height
        y2 = y + 100
        
        stair = Rectangle(Point(x1 , y1) , Point(x2 , y2))
        stair.fill_colour = colour
        stair.outline_colour = colour
        stair.outline_width = 0
        stair.draw(win)


def draw_solid_patch(win, x, y, colour):
    plain_patch = Rectangle(Point(x,y) , Point(x + 100, y + 100))
    plain_patch.fill_colour = colour
    plain_patch.outline_colour = colour
    plain_patch.outline_width = 0
    plain_patch.draw(win)


def draw_patch(win, x, y, size, row, col, colours):
    first_colour, second_colour, third_colour = colours


    if row == col:
        draw_last_digit_patch(win, x, y, first_colour)
        patch_states[(row, col)] = ("last", first_colour)
        
    elif (row == 0 and col > 0) or (col == size - 1 and row > 0):
        draw_last_digit_patch(win, x, y, second_colour)
        patch_states[(row, col)] = ("last", second_colour)
        
    elif (col == 0 and row > 0) or (row == size - 1 and col > 0):
        draw_solid_patch(win, x, y, third_colour)
        patch_states[(row, col)] = ("solid", third_colour)
        
    elif row < col:
        draw_solid_patch(win, x, y, second_colour)
        patch_states[(row, col)] = ("solid", second_colour)
        
    elif row > col:
        draw_penultimate_patch(win, x, y, third_colour)
        patch_states[(row, col)] = ("penultimate", third_colour)



#  FUNCTIONS FOR CHALLENGE 

def click_to_cell(x, y):
    return int(y // PATCH_SIZE), int(x // PATCH_SIZE)


def draw_border(win, r, c):
    global selection_border
    if selection_border:
        selection_border.undraw()

    x1 = c * 100
    y1 = r * 100
    x2 = x1 + 100
    y2 = y1 + 100

    border = Rectangle(Point(x1, y1), Point(x2, y2))
    border.outline_width = 5
    border.outline_colour = "black"
    border.fill_colour = "" 
    border.draw(win)
    selection_border = border


def erase_patch(win, r, c):
    rect = Rectangle(Point(c * 100, r * 100), Point(c * 100 + 100, r * 100 + 100))
    rect.fill_colour = "white"
    rect.outline_colour = "white"
    rect.outline_width = 0
    rect.draw(win)
    # Remove from patch states
    if (r, c) in patch_states:
        del patch_states[(r, c)]


def create_patch_here(win, r, c, colours, key):
    x = c * 100
    y = r * 100
    first_colour, second_colour, third_colour = colours

    if key == "1": 
        draw_penultimate_patch(win, x, y, first_colour)
        patch_states[(r, c)] = ("penultimate", first_colour)
    if key == "2": 
        draw_penultimate_patch(win, x, y, second_colour)
        patch_states[(r, c)] = ("penultimate", second_colour)
    if key == "3": 
        draw_penultimate_patch(win, x, y, third_colour)
        patch_states[(r, c)] = ("penultimate", third_colour)

    if key == "4": 
        draw_last_digit_patch(win, x, y, first_colour)
        patch_states[(r, c)] = ("last", first_colour)
    if key == "5": 
        draw_last_digit_patch(win, x, y, second_colour)
        patch_states[(r, c)] = ("last", second_colour)
    if key == "6": 
        draw_last_digit_patch(win, x, y, third_colour)
        patch_states[(r, c)] = ("last", third_colour)

    if key == "7": 
        draw_solid_patch(win, x, y, first_colour)
        patch_states[(r, c)] = ("solid", first_colour)
    if key == "8": 
        draw_solid_patch(win, x, y, second_colour)
        patch_states[(r, c)] = ("solid", second_colour)
    if key == "9": 
        draw_solid_patch(win, x, y, third_colour)
        patch_states[(r, c)] = ("solid", third_colour)


# MOVE FUNCTION for patches.
def move_patch(win, r, c, dr, dc, size):
    new_r = r + dr
    new_c = c + dc

    #check the borders that are they in grid(window)
    if not (0 <= new_r < size and 0 <= new_c < size):
        return r, c

    # check source patch and new postion empty.
    if (r, c) not in patch_states or (new_r, new_c) in patch_states:
        return r, c

    # get type and colour from patch state.
    patch_type, patch_colour = patch_states[(r, c)]
    
    # erase source patch
    erase_patch(win, r, c)
    
    # Draw patch for new position.
    x = new_c * 100
    y = new_r * 100
    
    if patch_type == "solid":
        draw_solid_patch(win, x, y, patch_colour)
    elif patch_type == "last":
        draw_final_patch(win, x, y, patch_colour)
    elif patch_type == "penultimate":
        draw_penultimate_patch(win, x, y, patch_colour)
    
    # add new position for patch state.
    patch_states[(new_r, new_c)] = (patch_type, patch_colour)
    return new_r, new_c


# ================= MAIN PROGRAM ==================

def main():
    global selected, patch_states, selection_border

    size = input_size()
    colours = input_three_colour()

    patch_states = {}

    win_size = size * 100
    win = Window("Patchwork Assignment", win_size, win_size)

    # background
    background = Rectangle(Point(0,0), Point(win_size, win_size))
    background.fill_colour = "white"
    background.outline_colour = "white"
    background.draw(win)

    # draw patchwork
    for row in range(size):
        for col in range(size):
            draw_patch(win, col * 100, row * 100, size, row, col, colours)

    selected = None
    
    while win.is_open():
        # Check for mouse click
        m = win.check_mouse()
        if m:
            r, c = click_to_cell(m.x, m.y)
            # Check if click is within valid grid bounds
            if 0 <= r < size and 0 <= c < size:
                selected = (r, c)
                draw_border(win, r, c)
       
        # Check for key press
        k = win.check_key()
        if k:
            if k == "Escape":
                selected = None
                if selection_border:
                    selection_border.undraw()
            
            elif selected:
                r, c = selected

                if k == "x": 
                    # Only delete if patch exists
                    if (r, c) in patch_states:
                        erase_patch(win, r, c)

                elif k in "123456789":
                    # Only create if empty
                    if (r, c) not in patch_states:
                        create_patch_here(win, r, c, colours, k)

                elif k in ["Up", "Down", "Left", "Right"]:
                    # Only move if patch exists
                    if (r, c) in patch_states:
                        if k == "Up":
                            r, c = move_patch(win, r, c, -1, 0, size)
                        elif k == "Down":
                            r, c = move_patch(win, r, c, 1, 0, size)
                        elif k == "Left":
                            r, c = move_patch(win, r, c, 0, -1, size)
                        elif k == "Right":
                            r, c = move_patch(win, r, c, 0, 1, size)

                selected = (r, c)
                draw_border(win, r, c)
             
             
    print("")            
    print("The code runs successfully")
    
    win.close()


main()

