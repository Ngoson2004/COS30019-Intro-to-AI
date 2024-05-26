from custom_search import Custom
from informed_search import Informed

#Beam search
class CUS2(Custom, Informed):
    def __init__(self):
        super().__init__()
        self.is_as = False
        self.level = [(tuple, [], [])]  # Each element is a tuple (node, path_to_node in direction, path to node in nodes)

    def search(self, grid_size, start, goals, obstacles):
        node_count = 0
        self.level = [(start, [], [])]
        while self.level:
            next_level = []
            for node, path, node_path in self.level:
                if node in goals:
                    self.path = node_path
                    return node, node_count, path  # Similarly, Beam search only retains the most promising node for each level, so the path is already optimised
                for dx, dy, dir in [(0, -1, "up"), (-1, 0, "left"), (0, 1, "down"), (1, 0, "right")]:
                    next_node = (node[0] + dx, node[1] + dy)
                    if 0 <= next_node[0] < grid_size[1] and 0 <= next_node[1] < grid_size[0] and next_node not in obstacles and next_node not in self.visited:
                        self.visited.append(next_node)
                        node_count += 1
                        next_level.append((next_node, path + [dir], node_path + [next_node]))

            # Sort by heuristic and keep the 3 best node
            next_level.sort(key=lambda x: self.heuristic(x[0], self.find_closest_goal(x[0], goals)))
            self.level = next_level[:3]     #set the beam width to 3

        return "No goal is reachable;", node_count, None