class Agent():
        # self.node_path = {start: None}     #dictionary to map nodes with their predecessors 
        # self.path = []      #return the path in array of nodes for visualisation
        # self.visited = [start]   #array to track all expanded nodes of an algo for visualisation
        # self.closest_goal = self.find_closest_goal(start, goals)  #tuple of the closest goal, apply for informed search

        # self.informed = False   #track whether we are using informed search
        # #for a-star
        # self.is_as = False      
        # self.g_score = {start: 0}   #accumulative g(n) heuristic
        # # for beam search
        # self.is_beam = False
        # self.level = [(start, [], [])]  # Each element is a tuple (node, path_to_node in direction, path to node in nodes)

    def __init__(self, strategy):
        self.strategy = strategy

    # uninformed search algos
    def perform_search(self, grid_size, start, goals, obstacles):
        return self.strategy.search(grid_size, start, goals, obstacles)


