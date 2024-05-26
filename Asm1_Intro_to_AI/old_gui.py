import tkinter as tk
import time

class GUI:
    def __init__(self, grid_size, start, goals, obstacles, strategy):

        #initiate the window 
        self.window = tk.Tk()
        self.window.title("Robot Navigation")

        #initiate the environment
        self.grid_size = grid_size
        self.start = start
        self.goals = goals
        self.obstacles = obstacles
        self.strategy = strategy

        #set basic information to create visualisation
        self.cell_size = 100
        self.canvas = tk.Canvas(self.window, width=self.grid_size[1] * self.cell_size,
                                height=self.grid_size[0] * self.cell_size)
        self.canvas.pack()
        self.set_up()
        self.start_search()

    def set_up(self):
        for i in range(self.grid_size[1]):
            for j in range(self.grid_size[0]):
                color = self.determine_node_color((i,j))
                self.canvas.create_rectangle(i * self.cell_size, j * self.cell_size,
                                             (i + 1) * self.cell_size, (j + 1) * self.cell_size, fill=color, outline="black")
                if self.strategy.informed:
                    self.label_cell((i,j))


    # initiate the visualisation by looping through each visited node
    def start_search(self):

        for node in self.strategy.visited:
            self.visualise_search(node)
            self.window.update_idletasks()  # Update the display
            time.sleep(0.5)  # Slow down the visualization, delay by 1 seconds each step

        self.highlight_final_path()

    # visualise each expanded node
    def visualise_search(self, node):
        x, y = node

        color = "red" if node==self.start else "yellow"

        self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                 (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                 fill=color, outline="black")
        
        if self.strategy.informed:
            self.label_cell(node)
        
            if self.strategy.is_beam:
                for state in self.strategy.level:
                    x ,y = state[0]
                    self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                            (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                            fill="deep sky blue", outline="black")
                    self.label_cell((x,y))
    
    def label_cell(self, node):
        x ,y = node
        heuristic_val = self.strategy.heuristic(node,self.strategy.find_closest_goal(node, self.goals))
        self.canvas.create_text((x + 0.5) * self.cell_size, (y + 0.1) * self.cell_size,
                                text=f"h(n): {heuristic_val}", font=('Arial', 14, 'bold'))
        
        if self.strategy.is_as:
            if node not in self.strategy.g_score.keys():
                pass
            else:
                self.canvas.create_text((x + 0.5) * self.cell_size, (y + 0.9) * self.cell_size,
                                        text=f"g(n): {self.strategy.g_score[node]}", font=('Arial', 14, 'bold'))

    def determine_node_color(self, node):
        if node == self.start:
            return 'red'
        elif node in self.goals and node not in self.obstacles and not self.strategy.informed:
            return 'green'
        elif node in self.goals and node != self.strategy.closest_goal and self.strategy.informed:
            return 'green'
        elif node in self.goals and node == self.strategy.closest_goal and self.strategy.informed:
            return 'blue'
        elif node in self.obstacles:
            return 'grey'  
        else:
            return 'white' # Grid color

    def highlight_final_path(self):
        # Highlight the final path if necessary
        path = self.strategy.path
        for node in path:
            x, y = node[0], node[1]
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                        (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                        fill="orange")
        
        self.window.after(5000, self.window.destroy)
    
    def mainloop(self):
        self.window.mainloop()