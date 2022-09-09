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
import draw as draw


# Initialize grid size from cmd line arguments
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

# Set start point
board[0][GRID_SIZE-1] = 2
# Set end point
board[GRID_SIZE-1][0] = 3
# 0 = EMPTY SPACE
# 1 = WALL
# 2 = START POINT
# 3 = END POINT


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
        draw.draw_board(pygame, SCREEN, board, cell_width, cell_height)

        # Draw grid overlay to screen
        draw.draw_grid_overlay(pygame, SCREEN, board, cell_width, cell_height)

        # Flip display
        pygame.display.flip()

    # Terminate program
    pygame.quit()

if __name__ == "__main__":
    print("Starting pathfinding algorithm visualizer")
    main()