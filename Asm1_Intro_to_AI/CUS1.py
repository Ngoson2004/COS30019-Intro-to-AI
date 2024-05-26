from custom_search import Custom

#Iterative Deepening Depth First Search
class CUS1(Custom):
    def __init__(self):
        super().__init__()
    
    def search(self, grid_size, start, goals, obstacles):

        node_count = 0
        for depth in range(grid_size[0]*grid_size[1]):     #maximum depth for the grid is equal to the total number of states in it
            self.visited.clear()    #Reset visited list for each depth
            result = self.dls(start, goals, depth, grid_size, obstacles, node_count)
            if result:
                return result   #return goal, node count and direction path

        return "No goal is reachable;", node_count, None
    
    #depth-limited search implementation. IDDFS is an extented version of DLS.
    def dls(self, node, goals, depth, grid_size, obstacles, node_count, node_path=[], path=[]):
        if depth == 0 and node in goals:
            self.path = node_path
            return node, node_count, path   #due to the selective and recursive approach of IDDFS, the path always retains the best directions. Thus, no need for backtracking from self.reconstruct_path(path,node)
        if depth > 0:
            self.visited.append(node)
            for dx, dy, dir in [(0, -1, "up"), (-1, 0, "left"), (0, 1, "down"), (1, 0, "right")]:   
                neighbor = (node[0] + dx, node[1] + dy)
                if 0 <= neighbor[0] < grid_size[1] and 0 <= neighbor[1] < grid_size[0] and neighbor not in obstacles and neighbor not in self.visited:
                    #self.get_direction(path, neighbor, dx, dy)
                    result = self.dls(neighbor, goals, depth - 1, grid_size, obstacles, node_count + 1, node_path + [neighbor], path + [dir])
                    #print(neighbor)
                    if result:
                        return result

        return None