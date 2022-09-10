# Name: Jonathan Dooley
# Date: 9/7/2022
# Description: An A* Pathfinding Algorithm visualizer
# Requirements:
#       -- Pygame
# CMD LINE ARGUMENTS:
#       -- 1. grid size
#   e.g. py main.py 20

import sys

import pygame
pygame.init()

import color_palette as colors
from settings import Settings
import util_functions as util
from board import Board


# Initialize grid size from cmd line arguments
if len(sys.argv) > 1:
    GRID_SIZE = int(sys.argv[1])
else:
    GRID_SIZE = 20


def main():
    """
    Runs the pygame clock, event handler, and main loop
    Args:
        N/A
    Returns:
        VOID
    """
    # Initialize global SCREEN and clock variables
    global SCREEN, CLOCK

    # Initialize screen resolution variables
    WIDTH = 500
    HEIGHT = 600

    # Set up display and clock
    SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
    CLOCK = pygame.time.Clock()

    # Initialize board resolution size variables
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 500

    # Intialize board info
    cell_height = BOARD_HEIGHT/GRID_SIZE
    cell_width = BOARD_WIDTH/GRID_SIZE

    # Initialize settings object
    settings = Settings(GRID_SIZE, WIDTH, HEIGHT, 
    BOARD_WIDTH, BOARD_HEIGHT, cell_width, cell_height)

    # Initialize board object
    board = Board(settings)

    # Initialize board
    board.array = [0] * GRID_SIZE
    for i in range(GRID_SIZE):
        board.array[i] = [0] * GRID_SIZE
    # Set start point
    board.array[0][GRID_SIZE-1] = 2
    # Set end point
    board.array[GRID_SIZE-1][0] = 3
    # 0 = EMPTY SPACE
    # 1 = WALL
    # 2 = START POINT
    # 3 = END POINT

    # Run until the user asks to quit
    running = True
    userDrawing = True
    mouseDown = False
    board_update_val = 0
    while running:
        """ Event Handler """
        for event in pygame.event.get():
            # Check if user clicked the quit button
            if event.type == pygame.QUIT:
                running = False

            # If the user clicks/drags the grid in drawing mode, update the board
            if userDrawing:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown = True
                    # If user left clicked : Draw square
                    if event.button == 1:
                        board_update_val = 1
                    
                    # If user right clicked : Erase square
                    elif event.button == 3:
                        board_update_val = 0

                elif event.type == pygame.MOUSEBUTTONUP:
                    mouseDown = False

                if mouseDown:
                    # get position of mouse cursor on click event
                    ( x, y ) = pygame.mouse.get_pos()

                    # if ( x , y ) is in grid
                    if x <= BOARD_WIDTH and y <= BOARD_HEIGHT:
                        # Get board coordinates of where user clicked
                        board_x, board_y = board.convert_screen_coords_to_board_coords(x, y)

                        # Update board with new walls
                        board.array[board_x][board_y] = board_update_val                        

        
        """ Drawing """
        # Fill the background with white
        SCREEN.fill(colors.BACKGROUND_COLOR)

        # Draw board to screen
        board.draw_board(SCREEN, board)

        # Draw grid overlay to screen
        board.draw_grid_overlay(SCREEN, board)

        # Flip display
        pygame.display.flip()

        board.print_board()
        print("\n\n\n")

    # Terminate program
    pygame.quit()

if __name__ == "__main__":
    print("Starting pathfinding algorithm visualizer")
    main()