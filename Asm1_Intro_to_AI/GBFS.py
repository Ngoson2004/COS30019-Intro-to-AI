from informed_search import Informed
from heapq import heappush, heappop

class GBFS(Informed):
    def __init__(self):
        super().__init__()
        self.is_as = False

    def search(self, grid_size, start, goals, obstacles):
        
        open_set = [(self.heuristic(start, self.find_closest_goal(start, goals)), start)]
        self.came_from = {start: None}
        self.node_path = {start: None}
        node_count = 0

        #print(closest_goal)

        while open_set:
            heuristic_val, current = heappop(open_set)

            if current in goals:
                self.path = self.reconstruct_path_node(self.node_path, current)
                return current, node_count, self.reconstruct_path(self.came_from, current)

            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)
                closest_goal = self.find_closest_goal(neighbor, goals)
                if 0 <= neighbor[0] < grid_size[1] and 0 <= neighbor[1] < grid_size[0] and neighbor not in self.visited and neighbor not in obstacles and self.heuristic(neighbor, closest_goal) < heuristic_val:
                    self.get_direction(self.came_from, neighbor, dx, dy)
                    self.visited.append(neighbor)
                    # print(neighbor)
                    self.node_path[neighbor] = current
                    heappush(open_set, (self.heuristic(neighbor, closest_goal), neighbor))
                    node_count += 1

        return "No goal is reachable;", node_count, None 