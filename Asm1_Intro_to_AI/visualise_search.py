from GUI import Interface
import pygame

class Visualise(Interface):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        super().__init__(grid_size, start, goals, obstacles, strategy)
        self.thick = 2


    def visualise_search(self, node, screen):
        x, y = node
        color = "red" if node == self.start else "yellow"  # Red if start, yellow otherwise

        #draw rect representing node expansion with 5px outline thickness
        pygame.draw.rect(screen, color, (x * (self.cell_size) + self.thick, y * (self.cell_size) + self.thick, 
                                                 self.cell_size - self.thick*2, self.cell_size - self.thick*2))
        
        if self.strategy.informed:
            self.label_cell(node, screen)
            

    def label_cell(self, node, screen):
        x, y = node
        heuristic_val = self.strategy.heuristic(node, self.strategy.find_closest_goal(node, self.goals))
        
        font = pygame.font.Font(None, 24)
        heuristic_text = font.render(f"h(n): {heuristic_val}", True, "black")
        screen.blit(heuristic_text, ((x + 0.3) * self.cell_size, (y + 0.1) * self.cell_size))
        
        if self.strategy.is_as and node in self.strategy.g_score:
            g_score_text = font.render(f"g(n): {self.strategy.g_score[node]}", True, "black")
            screen.blit(g_score_text, ((x + 0.3) * self.cell_size, (y + 0.8) * self.cell_size))

    def highlight_final_path(self, screen):
        path = self.strategy.path
        for node in path:
            x, y = node
            pygame.draw.rect(screen, (255, 165, 0), (x * (self.cell_size) + self.thick, y * (self.cell_size) + self.thick, 
                                                 self.cell_size - self.thick*2, self.cell_size - self.thick*2))  # Orange color for the path
        
        pygame.display.flip()
        pygame.time.delay(5000)  # Wait for 5 seconds
        pygame.quit()  # Close the pygame window and quit


