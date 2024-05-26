from queue import Queue
from uninformed_search import Uninformed

class BFS(Uninformed):
    def __init__(self):
        super().__init__()

    def search(self, grid_size, start, goals, obstacles):
        # Initialize the queue with the start position
        q = Queue()
        q.put(start)

        # create a dict to track path. 
        self.came_from = {start: None}
        self.node_path = {start: None}
        self.visited.append(start)
        node_count = 0
        
        while not q.empty():
            node = q.get()
            #print(f"Iter {node_count}: ", node)

            # Check if the node is one of the goals
            if node in goals:
                self.path = self.reconstruct_path_node(self.node_path, node)
                return node, node_count, self.reconstruct_path(self.came_from, node) #this is the path in direction

            # Explore neighbors 
            for dx,dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                neighbor = (node[0] + dx, node[1] + dy)
                if 0 <= neighbor[0] < grid_size[1] and 0 <= neighbor[1] < grid_size[0] and neighbor not in self.visited and neighbor not in obstacles:
                    #print("Changed node: ",neighbor, " Direction: ",(dx,dy))
                    self.get_direction(self.came_from, neighbor, dx, dy) # map cell changes to directions
                    self.visited.append(neighbor)
                    self.node_path[neighbor] = node
                    q.put(neighbor)
                    node_count += 1
                    
        return "No goal is reachable;", node_count, None  # No goal found        