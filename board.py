import pygame

import color_palette as colors
import util_functions as util

class Board:
    array = None

    def __init__(self, settings):
        self.settings = settings

    def convert_screen_coords_to_board_coords(self, x, y):
        x = util.floor_to_multiple(x, self.settings.cell_width)
        y = util.floor_to_multiple(y, self.settings.cell_height)
        return (int(x/self.settings.cell_width), int(y/self.settings.cell_height))
    
    def convert_board_coords_to_screen_coords(self, x, y):
        return (x*self.settings.cell_width, y*self.settings.cell_height)

    def print_board(self):
        for i in range(len(self.array)):
            row = ""
            for j in range(len(self.array[i])):
                row += str(self.array[i][j])
                row += " "
            print(row)

    
    def draw_board(self, SCREEN, board):
        """
        Draws the game board to the Pygame screen
        Args:
            pygame
            pygame screen module : SCREEN
            array : board
                -- 2D array containing board information
        Returns:
            VOID
        """
        for y in range(len(self.array)):
            for x in range(len(self.array[y])):
                # If board coordinate is a...
                # WALL
                cell_color = colors.BACKGROUND_COLOR
                if self.array[x][y] == 1:
                    cell_color = colors.WALL_COLOR

                # STARTPOINT
                elif self.array[x][y] == 2:
                    cell_color = colors.START_POINT_COLOR

                # ENDPOINT
                elif self.array[x][y] == 3:
                    cell_color = colors.END_POINT_COLOR

                coord_x, coord_y = self.convert_board_coords_to_screen_coords(x, y)
                pygame.draw.rect(SCREEN, cell_color, 
                    pygame.Rect(coord_x, coord_y, self.settings.cell_width, self.settings.cell_height))

    def draw_grid_overlay(self, SCREEN, board):
        """
        Draws the grid overlay to the Pygame screen
        Args:
            pygame
            pygame screen module -> SCREEN
            array : board
                -- 2D array containing board information
        Returns:
            VOID
        """
        for i in range(self.settings.GRID_SIZE):
                # Draw column
                column_start_x = (self.settings.cell_width*i) + self.settings.cell_width
                pygame.draw.line(SCREEN, colors.GRIDLINE_COLOR, 
                    (column_start_x, 0), (column_start_x, self.settings.BOARD_HEIGHT))
                
                # Draw row
                row_start_y = (self.settings.cell_height*i) + self.settings.cell_height
                pygame.draw.line(SCREEN, colors.GRIDLINE_COLOR, 
                    (0, row_start_y), (self.settings.WIDTH, row_start_y))