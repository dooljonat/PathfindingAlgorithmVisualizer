# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# https://en.wikipedia.org/wiki/A*_search_algorithm
# https://www.youtube.com/watch?v=-L-WgKMFuhE
import pygame
import color_palette as colors
import util_functions as util


# TODO: YOUR LOGIC IN THE ASTAR CODE IS BROKEN. THE PROGRAM CHECKS SPOTS ITS ALREADY CHECKED MULTIPLE TIMES

class Node:
    """ Node object for A* pathfinding. Stores position, parent, and g,h,f costs """
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    # Compares current & other node's positions
    def __eq__(self, other):
        return self.position == other.position
    
    def __hash__(self):
        return hash(str(self))

# def backtrack_nodes(current_node):
#     """ Backtracks from current (target node) and finding parents of nodes until
#          no parent exists (start node), returns list of positions indicating shortest path"""
#     path = []
#     current = current_node
#     while current is not None:
#         path.append(current.position)
#         current = current.parent
#     return path.reverse()


def astar(SCREEN, settings, board, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given board"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = set()
    closed_list = set()

    # Add the start node
    open_list.add(start_node)

    # List of walkable terrain values
    walkable = [0,2,3]

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = list(open_list)[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.remove(current_node)
        closed_list.add(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(board) - 1) or node_position[0] < 0 or node_position[1] > (len(board) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if board[node_position[0]][node_position[1]] not in walkable:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.add(child)
            coord_x, coord_y = util.convert_board_coords_to_screen_coords(child.position[0], child.position[1], 
            settings.cell_width, settings.cell_height)
            pygame.draw.rect(SCREEN, colors.PATH_COLOR, 
                pygame.Rect(coord_x, coord_y, settings.cell_width, settings.cell_height))

            
    
    