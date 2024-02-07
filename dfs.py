from MazeProblem.maze import *
from MazeProblem.Stack import Stack
import time

# create a stack
stack = Stack()

# create list to store visited nodes
visited_list = []

def neighbour_nodes(current_node):
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
    neighbors.sort(reverse=True)

    for neighbor in neighbors:
        # if the neighbour is valid, push to the stack
        if is_valid_move(neighbor, current_node, barrier_set):
            stack.push(neighbor, neighbor // 6, neighbor % 6)

# find the start node
visiting_node = maze.head
while visiting_node:
    if visiting_node.value == start_node:
        stack.push(visiting_node.value, visiting_node.x_coordinate, visiting_node.y_coordinate)
        break
    visiting_node = visiting_node.next

# DFS algorithm
def dfs(goal_node):
    # capture algorithm start time
    dfs_start_time = time.time_ns()
    while not stack.is_empty():
        # explore top of the stack
        visiting_node = stack.peek()
        stack.pop()
        if visiting_node.value not in visited_list:
            visited_list.append(visiting_node.value)
            if visiting_node.value == goal_node:
                break
            # check for neighbour nodes and add it to the stack
            neighbour_nodes(visiting_node)
    # capture finishing time
    dfs_end_time = time.time_ns()
    dfs_run_time = dfs_end_time - dfs_start_time

    # print the maze with the path
    print('\u001B[35mMaze with final path in using DFS\u001B[39m')
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
        elif current_node.value in visited_list:
            print('\u001B[34m.    \u001B[39m', end="")
        else:
            print('.    ', end="")
        if value_count % 6 == 0:
            print('\n')
        value_count += 1
        current_node = current_node.next

    print("Total nodes explored:", len(visited_list))
    print("Visited nodes list:", visited_list)
    print("Time to find the goal:", dfs_run_time, "ns")
