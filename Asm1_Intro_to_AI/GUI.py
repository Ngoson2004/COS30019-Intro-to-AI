from abc import ABC, abstractmethod
import pygame
import os

class Interface(ABC):
    def __init__(self, grid_size, start, goals, obstacles, strategy):
        pygame.init()
        
        self.grid_size = grid_size
        self.start = start
        self.goals = goals
        self.obstacles = obstacles
        self.strategy = strategy
        self.cell_size = 100

        # Load and play background music
        music_path = os.path.join('.', 'Resonance.mp3') #Home (2014). Resonance. [Odyssey] Midwest Collective. Available at: https://www.youtube.com/watch?v=8GW6sLrK40k [Accessed 19 Apr. 2024].
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Loop music


