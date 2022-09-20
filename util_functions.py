import math

# Floor a number to an interval
def floor_to_multiple(number, multiple):
    return multiple * math.floor(number / multiple)

def convert_screen_coords_to_board_coords(x, y, cell_width, cell_height):
    x = floor_to_multiple(x, cell_width)
    y = floor_to_multiple(y, cell_height)
    return (int(x/cell_width), int(y/cell_height))

def convert_board_coords_to_screen_coords(x, y, cell_width, cell_height):
    return (x*cell_width, y*cell_height)