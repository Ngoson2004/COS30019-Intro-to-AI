from uninformed_search import Uninformed

class DFS(Uninformed):
    def __init__(self):
        super().__init__()

    def search(self, grid_size, start, goals, obstacles):
        stack = [start]
        self.came_from = {start: None}
        self.node_path = {start: None}
        node_count = 0

        while stack:
            node = stack.pop()

            if node not in self.visited:
                self.visited.append(node)
            if node in goals:
                self.path = self.reconstruct_path_node(self.node_path, node)
                return node, node_count, self.reconstruct_path(self.came_from, node)

            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                neighbor = (node[0] + dx, node[1] + dy)
                if 0 <= neighbor[0] < grid_size[1] and 0 <= neighbor[1] < grid_size[0] and neighbor not in self.visited and neighbor not in obstacles:
                    self.get_direction(self.came_from, neighbor, dx, dy)
                    self.node_path[neighbor] = node
                    stack.append(neighbor)
                    self.visited.append(neighbor)
                    node_count += 1

        return "No goal is reachable;", node_count, None 