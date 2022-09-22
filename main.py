# Name: Jonathan Dooley
# Date: 9/7/2022
# Description: An A* Pathfinding Algorithm visualizer
# Requirements:
#       -- pygame
#       -- pygame-widgets
# CMD LINE ARGUMENTS:
#       -- 1. grid size
#   e.g. py main.py 20

import sys

import pygame
import threading

import color_palette as colors
from settings import Settings
import util_functions as util
from board import Board
from ui_obj import Button
from search_algorithms import astar_search
from enum import Enum
import visualizer as vis

pygame.init()

# Initialize grid size from cmd line arguments
if len(sys.argv) > 1:
    GRID_SIZE = int(sys.argv[1])
else:
    GRID_SIZE = 20

# Program state
class ProgramState(Enum):
    USER_DRAWING = 0
    PATHFINDING = 1
    PATHFOUND = 2


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
    start_point = (0, GRID_SIZE-1)
    print(start_point)
    board.array[0][GRID_SIZE-1] = 2
    # Set end point
    end_point = (GRID_SIZE-1, 0)
    print(end_point)
    board.array[GRID_SIZE-1][0] = 3
    # 0 = EMPTY SPACE
    # 1 = WALL
    # 2 = START POINT
    # 3 = END POINT

    # Initialize button objects
    stopButton = Button(settings, 20, 520, 80, 50, 
        colors.DRAW_BUTTON_COLOR, colors.DRAW_HOVER_COLOR, colors.DRAW_OUTLINE_COLOR, 
        "Stop")
    startButton = Button(settings, 20, 520, 80, 50, 
        colors.START_BUTTON_COLOR, colors.START_HOVER_COLOR, colors.START_OUTLINE_COLOR, 
        "Start")

    # Run until the user asks to quit
    running = True
    mouseDown = False
    board_update_val = 0
    programState = ProgramState.USER_DRAWING
    while running:
        """ Event Handler """
        events = pygame.event.get()
        for event in events:
            ( x, y ) = pygame.mouse.get_pos()

            # Check if user clicked the quit button
            if event.type == pygame.QUIT:
                running = False

            if programState == ProgramState.USER_DRAWING:
                if startButton.isMouseOver(x, y):
                    startButton.isHover = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        startButton.isHover = False
                        programState = ProgramState.PATHFINDING

                # If the user clicks/drags the grid in drawing mode, update the board
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
                    # if ( x , y ) is in grid
                    if x <= BOARD_WIDTH-1 and y <= BOARD_HEIGHT-1:
                        # Get board coordinates of where user clicked
                        board_x, board_y = util.convert_screen_coords_to_board_coords(x, y, 
                            settings.cell_width, settings.cell_height)

                        # Update board with new walls
                        board.array[board_x][board_y] = board_update_val

            elif programState == ProgramState.PATHFINDING:
                if stopButton.isMouseOver(x, y):
                    stopButton.isHover = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        stopButton.isHover = False
                        programState = ProgramState.USER_DRAWING
                else:
                    stopButton.isHover = False

                path = astar_search(board.array, start_point, end_point)
                if path:
                    path.pop(-1)
                    programState = ProgramState.PATHFOUND
                else:
                    print("NO VALID PATH ATTAINABLE")
                    programState = ProgramState.USER_DRAWING

            elif programState == ProgramState.PATHFOUND:
                if stopButton.isMouseOver(x, y):
                    stopButton.isHover = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        stopButton.isHover = False
                        programState = ProgramState.USER_DRAWING
                        path = None
                else:
                    stopButton.isHover = False 

        """ Drawing to screen """
        # Fill the background with white
        SCREEN.fill(colors.BACKGROUND_COLOR)

        # Draw board to screen
        board.draw_board(SCREEN, board, start_point, end_point)

        # Draw grid overlay to screen
        board.draw_grid_overlay(SCREEN, board)

        # Draw UI
        if programState == ProgramState.USER_DRAWING:
            startButton.draw(SCREEN)
            font = pygame.font.SysFont('georgia', 12)
            text = font.render("Left click to draw, right click to erase", 1, (0,0,0))
            SCREEN.blit(text, (270, 540))
        else:
            stopButton.draw(SCREEN)

        # Draw path + visualizer
        if programState == ProgramState.PATHFOUND:
            vis.draw_path(SCREEN, settings, path)

        # Flip display
        pygame.display.flip()

        # TODO: LOOK INTO THREADING TO PREVENT FREEZING

    # Terminate program
    pygame.quit()


if __name__ == "__main__":
    print("Starting pathfinding algorithm visualizer")
    main()