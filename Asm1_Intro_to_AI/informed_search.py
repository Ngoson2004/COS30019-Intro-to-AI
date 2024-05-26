from abc import ABC, abstractmethod
from uninformed_search import Uninformed

class Informed(Uninformed):
    def __init__(self):
        super().__init__()
        self.informed = True    #to notify the GUI that this is informed search
        self.closest_goal = tuple   #to store the closest goal to the current state
        # self.node_path = {self.start: None}     #dictionary to map nodes with their predecessors 
        # self.path = []      #return the path in array of nodes for visualisation
        # self.visited = [self.start]   #array to track all expanded nodes of an algo for visualisation

    @abstractmethod  
    def search(self, grid_size, start, goals, obstacles):
        pass

    #find the closest goal to the starting point 
    def find_closest_goal(self, node, goals):
        self.closest_goal = goals[0]

        #check the heuristic value of every goal. Return the goal with lowest value.
        for i in range(len(goals)):
            if self.heuristic(node, goals[i]) < self.heuristic(node, self.closest_goal):
                self.closest_goal = goals[i]

        return self.closest_goal
    
    #heuristic function, evaluating distance from cell to goal
    def heuristic(self, node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])     #Manhattan distance