import heapq

def heuristic(a, b):
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)

def astar_search(board_array, start, goal):
    # Directions to look for neighbors
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set() # Set of closed position
    came_from = {}    # Dict of where nodes came from, e.g. parents of nodes

    # Intialize gscore and fscore dicts with start position's values
    gscore = {start:0} 
    fscore = {start:heuristic(start, goal)}

    # Initialize heap (Priority queue)
    #   -> Priority queues associate each value with a "priority"
    #      popping an item from a priority queue will always give you the item with the lowest priority
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
    while oheap:
        # Get the current position
        # (position with lowest f score)
        current = heapq.heappop(oheap)[1]

        # The program found the target
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1]

        # Get neighbors of current position and push them to the heap IF
        #  1. they are within the boundaries of the board
        #  2. they are on walkable terrain
        #  3. they are not in the set of already closed positions
        #  4. their tentative_gscore is less than gscore of neighbor(if it currently exists in dict) 
        #     OR neighbor is not currently in the priority queue oheap
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            # g = how far away neighbor is from starting position
            tentative_g_score = gscore[current] + heuristic(current, neighbor) 
 
            if neighbor[0] > len(board_array)-1 or neighbor[0] < 0 or neighbor[1] > len(board_array)-1 or neighbor[1] < 0:
                continue

            if board_array[neighbor[0]][neighbor[1]] == 1:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
            print("tentative: ", tentative_g_score)
            print("current position: {0} {1}".format(current[0], current[1]))
            print("neighbor's g_score: ", gscore.get(neighbor, 0))
            print("neighbor's position: {0} {1}".format(neighbor[0], neighbor[1]))
            print()
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current # Set the neighbor's parent as the current position
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
 

    return False
