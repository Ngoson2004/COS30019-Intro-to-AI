from GUI import Interface
from visualise_search import Visualise
import pygame


class Event(Interface):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        super().__init__(grid_size, start, goals, obstacles, strategy)
        self.active = False
        self.paused = False
        self.visual = Visualise(grid_size, start, goals, obstacles, strategy)

    def handle_mouse_event(self, event, height, screen):
        x, y = event.pos
        # Check if 'Start' button is clicked
        if (10 <= x <= 90 and height - 90 <= y <= height - 60):
            self.start_search(height, screen)

    def start_search(self, height, screen):
        if not self.active:
            self.active = True
            self.paused = False

            for node in self.strategy.visited:
                if not self.active:
                    break

                while self.paused:
                    self.wait_until_resumed(height)

                self.handle_events(height)
                self.visual.visualise_search(node, screen)      #visualise node expansion
                pygame.display.flip()   # Update the display
                pygame.time.delay(500)  # Slow down the visualization, delay by 500 milliseconds each step

            if self.active:             # If the search was not stopped, after showing the expanded nodes, highlight the final path
                self.visual.highlight_final_path(screen)    #highlight the path to goal after finishing search

    def handle_events(self, height):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #handle stop button
                if 310 <= x <= 390 and height - 90 <= y <= height - 60:
                    self.active = False     #reset everything
                #handle pause button
                elif 610 <= x <= 690 and height - 90 <= y <= height - 60:
                    self.paused = True


    def wait_until_resumed(self, height):
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    #if resume button is pressed
                    if 910 <= x <= 990 and height - 90 <= y <= height - 60:  # Check if 'Resume' button is clicked
                        self.paused = False
                    #if stop button is pressed
                    if 310 <= x <= 390 and height - 90 <= y <= height - 60:  # Optionally allow stopping during pause
                        self.active = False 
                        self.paused = False


