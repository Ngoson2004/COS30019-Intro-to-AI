from abc import ABC, abstractmethod

class Uninformed(ABC):
    def __init__(self):
        super().__init__()
        self.node_path = dict    #dictionary to map nodes with their predecessors 
        self.came_from = dict   #dictionary used to store directions in correspondance with a newly explore node
        self.path = []      #return the path in array of nodes for visualisation
        self.visited = []   #array to track all expanded nodes of an algo for visualisation
        self.informed = False          #to notify the GUI that this is not informed search

    @abstractmethod
    def search(self, grid_size, start, goals, obstacles):
        super().search(grid_size, start, goals, obstacles)

    def reconstruct_path(self, came_from, goal):
        map_direction = {(1,0): 'right', (-1,0): 'left', (0,1): 'down', (0,-1):'up'}
        current = goal
        path = []
        while current in came_from and came_from[current] is not None:
            path.append(came_from[current])
            # Find the previous node based on the direction
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                if map_direction[(dx, dy)] == came_from[current]:
                    current = (current[0] - dx, current[1] - dy)
                    break
        return path[::-1]  # Reverse the path to start from the beginning
    
    #backtrack the shortest path
    def reconstruct_path_node(self, node_track, goal):
        current = goal
        path = []
        while current:
            path.append(current)
            current = node_track[current]
        
        return path[::-1]
    
    # function map cell changes to directions and update path tracking dict    
    def get_direction(self, came_from, node, dx, dy):
        map_direction = {(1,0): 'right', (-1,0): 'left', (0,1): 'down', (0,-1):'up'}
        came_from[node] = map_direction[(dx,dy)]