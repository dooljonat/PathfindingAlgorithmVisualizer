import pygame

import color_palette as colors
import util_functions as util

class Board:
    array = None

    def __init__(self, settings):
        self.settings = settings

    def print_board(self):
        for i in range(len(self.array)):
            row = ""
            for j in range(len(self.array[i])):
                row += str(self.array[i][j])
                row += " "
            print(row)

    def draw_board(self, SCREEN, board, start_point, end_point):
        """
        Draws the game board to the Pygame screen
        Args:
            pygame
            pygame screen module : SCREEN
            array : board
                -- 2D array containing board information
            start_point: tuple
                -- tuple containing start point coordinates
            end_point: tuple
                -- tuple containing end point coordinates
        Returns:
            VOID
        """
        for y in range(len(self.array)):
            for x in range(len(self.array[y])):
                if self.array[x][y] == 0:
                    continue

                cell_color = None
                coord_x, coord_y = util.convert_board_coords_to_screen_coords(x, y, self.settings.cell_width, self.settings.cell_height)

                # Pick color to draw
                if self.array[x][y] == 1:
                    cell_color = colors.WALL_COLOR
                elif x == start_point[0] and y == start_point[1]:
                    cell_color = colors.START_POINT_COLOR
                elif x == end_point[0] and y == end_point[1]:
                    cell_color = colors.END_POINT_COLOR
                                
                # Draw rect
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