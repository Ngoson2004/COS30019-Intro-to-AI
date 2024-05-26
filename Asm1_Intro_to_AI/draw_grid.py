import pygame
from GUI import Interface

class Grid(Interface):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        super().__init__(grid_size, start, goals, obstacles, strategy)
        self.thick = 2

    def draw_grid(self, screen):
       for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                color = self.determine_node_color((i, j))   #automatically determine color of state
                pygame.draw.rect(screen, color, (i * (self.cell_size) + self.thick, j * (self.cell_size) + self.thick, 
                                                 self.cell_size - self.thick*2, self.cell_size - self.thick*2))   #draw grid with 2px thick border
                
                if self.strategy.informed:
                    self.label_cell((i,j), screen)
            

    def label_cell(self, node, screen):
        x, y = node
        heuristic_val = self.strategy.heuristic(node, self.strategy.find_closest_goal(node, self.goals))
        
        font = pygame.font.Font(None, 24)
        heuristic_text = font.render(f"h(n): {heuristic_val}", True, "black")
        screen.blit(heuristic_text, ((x + 0.3) * self.cell_size, (y + 0.1) * self.cell_size))
        
        if self.strategy.is_as and node in self.strategy.g_score:
            g_score_text = font.render(f"g(n): {self.strategy.g_score[node]}", True, "black")
            screen.blit(g_score_text, ((x + 0.3) * self.cell_size, (y + 0.8) * self.cell_size))

    def determine_node_color(self, node):
        if node == self.start:
            return 'red'
        elif node in self.goals:
            return 'green'
        elif node in self.goals and node != self.strategy.closest_goal and self.strategy.informed:
            return 'green'
        elif node in self.goals and node == self.strategy.closest_goal and self.strategy.informed:
            return 'blue'
        elif node in self.obstacles:
            return 'grey'
        else:
            return 'white'