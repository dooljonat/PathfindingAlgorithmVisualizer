import pygame
import color_palette as colors
import util_functions as util

def draw_path(SCREEN, settings, path):
    for pos in path:
        coord_x, coord_y = util.convert_board_coords_to_screen_coords(pos[0], pos[1], 
            settings.cell_width, settings.cell_height)
                        
        # Draw rect
        pygame.draw.rect(SCREEN, colors.PATH_COLOR, 
                pygame.Rect(coord_x, coord_y, settings.cell_width, settings.cell_height))