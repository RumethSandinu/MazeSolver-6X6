from MazeProblem.maze import *
from MazeProblem.dfs import *
from MazeProblem.a_star import *

# print the maze
print_setup_maze(maze)

# permform DFS and print
dfs(goal_node)

# perform A*
a_star_start_time = time.time_ns()
path = a_star(maze, start_node, goal_node, barrier_set)
a_star_end_time = time.time_ns()
a_star_run_time = a_star_end_time - a_star_start_time

# print the maze with the path
print('\n\u001B[35mMaze with final path using A*\u001B[39m')
print()
current_node = maze.head
value_count = 1
while current_node:
    if current_node.value == start_node:
        print('\u001B[34mS    \u001B[39m', end="")
    elif current_node.value == goal_node:
        print('\u001B[34mG    \u001B[39m', end="")
    elif current_node.value in barrier_set:
        print('\u001B[31mB    \u001B[39m', end="")
    elif current_node.value in path:
        print('\u001B[34m.    \u001B[39m', end="")
    else:
        print('.    ', end="")
    if value_count % 6 == 0:
        print('\n')
    value_count += 1
    current_node = current_node.next

print("Total nodes explored:", len(path))
print('Visited node list : ', end='')
print(path)
print("Time to find the goal : ", a_star_run_time, "ns")
