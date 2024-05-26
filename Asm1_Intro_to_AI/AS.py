from informed_search import Informed
from heapq import heappush, heappop

class AS(Informed):
    def __init__(self):
        super().__init__()
        self.g_score = {tuple: 0}   #accumulative g(n) heuristic
        self.is_as = True   #to notify the GUI that this is A-star

    def search(self, grid_size, start, goals, obstacles):
        # print(self.closest_goal)

        open_set = [(self.heuristic(start, self.find_closest_goal(start, goals)), start)]
        self.came_from = {start: None}
        self.node_path = {start: None}
        self.g_score = {start: 0} 

        node_count = 0

        while open_set:
            heuristic_val, current = heappop(open_set)

            if current in goals:
                self.path = self.reconstruct_path_node(self.node_path, current)
                return current, node_count, self.reconstruct_path(self.came_from, current)

            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)
                tentative_g_score = self.g_score[current] + 1
                closest_goal = self.find_closest_goal(neighbor, goals)
                if 0 <= neighbor[0] < grid_size[1] and 0 <= neighbor[1] < grid_size[0] and neighbor not in self.visited and neighbor not in obstacles and tentative_g_score + self.heuristic(neighbor, closest_goal) < self.g_score.get(neighbor, float("inf")) + heuristic_val:
                        # print(g_score, tentative_g_score)
                        self.get_direction(self.came_from, neighbor, dx, dy)
                        self.visited.append(neighbor)
                        self.g_score[neighbor] = tentative_g_score
                        self.node_path[neighbor] = current
                        heappush(open_set, (tentative_g_score + self.heuristic(neighbor, closest_goal), neighbor))
                        node_count += 1

        return "No goal is reachable;", node_count, None 
    