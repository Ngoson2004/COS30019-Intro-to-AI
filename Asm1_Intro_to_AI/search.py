from BFS import BFS
from DFS import DFS
from GBFS import GBFS
from AS import AS
from CUS1 import CUS1
from CUS2 import CUS2
from agent import Agent
from initiator import Init
from draw_grid import Grid
# from button_handler import Button
from event_handler import Event
from visualise_search import Visualise
from load_file import load_file
import sys
    

def main(filename, method):
    try:
        grid, start, goal, obstacles = load_file(filename)
    except:     #handle invalid file's format
        print("Please review file's format or dir")

    if method.lower() == "bfs":
        strategy = BFS()
    elif method.lower() == "dfs":
        strategy = DFS()
    elif method.lower() == "gbfs":
        strategy = GBFS()
    elif method.lower() == 'as':
        strategy = AS()
    elif method.lower() == 'cus1':
        strategy = CUS1()
    elif method.lower() == 'cus2':
        strategy = CUS2()
    else:
        print("Invalid method. Please use 'bfs', 'dfs', 'as', 'gbfs', 'cus1' or 'cus2'.")
        return

    agent = Agent(strategy)
    try:
        node, node_count, path = agent.perform_search(grid, start, goal, obstacles)
    except:
        return

    #print the outputs on the terminal
    print(filename, method)
    print(node, node_count)
    if path is not None:
        print(path)

    # set up GUI
    event = Event(grid, start, goal, obstacles, strategy)
    grid = Grid(grid, start, goal, obstacles, strategy)
    GUI_instance = Init(grid, event)
    GUI_instance.run()
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
    else:
        main(sys.argv[1], sys.argv[2])