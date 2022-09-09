import color_palette as colors

def draw_board(pygame, SCREEN, board, cell_width, cell_height):
    """
    Draws the game board to the Pygame screen
    Args:
        pygame
        pygame screen module : SCREEN
        array : board
            -- 2D array containing board information
        int : cell_width
            -- The width of each cell in the grid in pixels
        int : cell_height
            -- The height of each cell in the grid in pixels  
    Returns:
        VOID
    """
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

def draw_grid_overlay(pygame, SCREEN, board, GRID_SIZE, cell_width, cell_height, WIDTH, HEIGHT):
    """
    Draws the grid overlay to the Pygame screen
    Args:
        pygame
        pygame screen module -> SCREEN
        array : board
            -- 2D array containing board information
        int : GRID_SIZE
            -- :e size of the (square) grid in cells
        int : cell_width
            -- The width of each cell in the grid in pixels
        int : cell_height
            -- The height of each cell in the grid in pixels  
        int : WIDTH
            -- The width of the screen in pixels
        int : HEIGHT 
            -- The height of the screen in pixels
    Returns:
        VOID
    """
    for i in range(GRID_SIZE):
            # Draw column
            column_start_x = (cell_width*i) + cell_width
            pygame.draw.line(SCREEN, colors.GRIDLINE_COLOR, 
                (column_start_x, 0), (column_start_x, HEIGHT))
            
            # Draw row
            row_start_y = (cell_height*i) + cell_height
            pygame.draw.line(SCREEN, colors.GRIDLINE_COLOR, 
                (0, row_start_y), (WIDTH, row_start_y))