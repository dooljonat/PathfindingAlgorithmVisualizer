# Name: Jonathan Dooley
# Date: 9/7/2022
# Description: An A* Pathfinding Algorithm visualizer
# Requirements:
#       -- Pygame
# CMD LINE ARGUMENTS:
#       -- 1. rows
#       -- 2. columns
#   e.g. py main.py 20 20

import sys

import pygame
pygame.init()

import color_palette as colors


# Initialize grid size from cmd line arguments
# TODO: CHECK IF CMD LINE ARGS EXIST FIRST, SET DEFAULT AS 20
if len(sys.argv) > 1:
    GRID_SIZE = int(sys.argv[1])
else:
    GRID_SIZE = 20
# Initialize board
# TODO: Make this editable by the user, e.g. rows and columns
#       (not predefined)
board = [0] * GRID_SIZE
for i in range(GRID_SIZE):
    board[i] = [0] * GRID_SIZE
# 0 = EMPTY SPACE
# 1 = WALL
# 2 = START POINT
# 3 = END POINT

# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,],
#     [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#     [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
# ]

def main():
    # Initialize global SCREEN and clock variables
    global SCREEN, CLOCK

    # Initialize screen resolution variables
    WIDTH = 500
    HEIGHT = 500

    # Set up display and clock
    SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
    CLOCK = pygame.time.Clock()

    # Intialize board info
    cell_height = HEIGHT/GRID_SIZE
    cell_width = WIDTH/GRID_SIZE

    # Run until the user asks to quit
    running = True
    while running:
        # Event handler
        for event in pygame.event.get():
            # Check if user clicked the quit button
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        SCREEN.fill(colors.BACKGROUND_COLOR)

        # Draw board to screen
        for y in range(len(board)):
            for x in range(len(board[y])):
                # If board coordinate is a...
                # WALL
                if board[x][y] == 1:
                    coord_x = x*cell_width
                    coord_y = y*cell_height
                    pygame.draw.rect(SCREEN, colors.WALL_COLOR, 
                        pygame.Rect(coord_x, coord_y, cell_width, cell_height))
                # STARTPOINT
                elif board[x][y] == 2:
                    coord_x = x*cell_width
                    coord_y = y*cell_height
                    pygame.draw.rect(SCREEN, colors.START_POINT_COLOR, 
                        pygame.Rect(coord_x, coord_y, cell_width, cell_height))
                # ENDPOINT
                elif board[x][y] == 3:
                    coord_x = x*cell_width
                    coord_y = y*cell_height
                    pygame.draw.rect(SCREEN, colors.END_POINT_COLOR, 
                        pygame.Rect(coord_x, coord_y, cell_width, cell_height))

        # Draw grid overlay to screen
        for i in range(GRID_SIZE):
            # Draw column
            column_start_x = (cell_width*i) + cell_width
            pygame.draw.line(SCREEN, colors.GRIDLINE_COLOR, 
                (column_start_x, 0), (column_start_x, HEIGHT))
            
            # Draw row
            row_start_y = (cell_height*i) + cell_height
            pygame.draw.line(SCREEN, colors.GRIDLINE_COLOR, 
                (0, row_start_y), (WIDTH, row_start_y))


        # Flip display
        pygame.display.flip()

    # Terminate program
    pygame.quit()

if __name__ == "__main__":
    print("Starting pathfinding algorithm visualizer")
    main()