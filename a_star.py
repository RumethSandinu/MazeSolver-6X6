from MazeProblem.maze import *

def neighbour_nodes(current_node, barrier_set):
    neighbour_nodes = []
    neighbors = [
        current_node.value + 7,
        current_node.value + 6,
        current_node.value + 5,
        current_node.value + 1,
        current_node.value - 1,
        current_node.value - 5,
        current_node.value - 6,
        current_node.value - 7
    ]
    for neighbor in neighbors:
        # if neighbour is valid append to the neighbour_nodes list
        if is_valid_move(neighbor, current_node, barrier_set):
            neighbour_nodes.append(maze.find_node(neighbor))
    return neighbour_nodes

# calculate heuristic cost using manhattan distance
def manhattan_distance(node, goal_node):
    return abs(node.x_coordinate - goal_node.x_coordinate) + abs(node.y_coordinate - goal_node.y_coordinate)

# A* algorithm
def a_star(maze, start_node, goal_node, barrier_set):
    # create open and closed set
    open_set = set()
    closed_set = set()

    # find start and goal nodes
    start = maze.find_node(start_node)
    goal = maze.find_node(goal_node)

    # cost for the start node
    start.cost = 0
    # heuristic cost for the start node
    start.heuristic_cost = manhattan_distance(start, goal)
    open_set.add(start)

    while open_set:
        # get the node with the lowest cost + heuristic_cost from the open set
        current = min(open_set, key=lambda node: node.cost + node.heuristic_cost)
        if current == goal:
            path = []
            while current:
                path.append(current.value)
                current = current.parent
            return path[::-1]

        # remove the current node from the open set and add it to the closed set
        open_set.remove(current)
        closed_set.add(current)

        for neighbor in neighbour_nodes(current, barrier_set):
            # skip the neighbours in closed list nad barriers
            if neighbor in closed_set or neighbor.value in barrier_set:
                continue

            # calculate path cost
            path = current.cost + 1

            # if the neighbor is not in the open set or the lowest path cost
            if neighbor not in open_set or path < neighbor.cost:
                # update neighbor parent, cost, and heuristic cost
                neighbor.parent = current
                neighbor.cost = path
                neighbor.heuristic_cost = manhattan_distance(neighbor, goal)
                # add neighbor to the open set if it is not there
                if neighbor not in open_set:
                    open_set.add(neighbor)
    # if the goal not found
    return None


