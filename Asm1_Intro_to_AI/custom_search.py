from abc import ABC, abstractmethod
from uninformed_search import Uninformed

class Custom(Uninformed):
    def __init__(self):
        super().__init__()

    @abstractmethod  
    def search(self, grid_size, start, goals, obstacles):
        pass