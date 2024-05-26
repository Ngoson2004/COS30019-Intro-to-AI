def load_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines() # read file line by line
    
    #define environment 
    grid_size = tuple(map(int, lines[0].strip().strip('[]').split(',')))
    start = tuple(map(int, lines[1].strip().strip('()').split(',')))
    goals = [tuple(map(int, goal.strip().strip('()').split(','))) for goal in lines[2].split('|')]
    
    obstacles = []
    for line in lines[3:]:
        x, y, w, h = map(int, line.strip().strip('()').split(','))
        for i in range(x, x + w):
            for j in range(y, y + h):
                obstacles.append((i, j))
    # print(obstacles)

    return grid_size, start, goals, obstacles