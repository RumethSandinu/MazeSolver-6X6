import random
from MazeProblem.LinkedList import LinkedList

# set up the maze
maze = LinkedList()
coordinate_number = 36

for i in range(0, 6):
    k = 0
    for j in range(i, coordinate_number, 6):
        maze.append(j, i, k)
        k+=1


# initialize start node and goal node with random values
start_node = random.randint(0, 11)
goal_node = random.randint(24, 35)

# initialize barriers with random values
barrier_1 = random.randint(0, 35)
while barrier_1 == start_node or barrier_1 == goal_node:
    barrier_1 = random.randint(0, 35)

barrier_2 = random.randint(0, 35)
while barrier_2 == start_node or barrier_2 == goal_node or barrier_2 == barrier_1:
    barrier_2 = random.randint(0, 35)

barrier_3 = random.randint(0, 35)
while barrier_3 == start_node or barrier_3 == goal_node or barrier_3 == barrier_1 or barrier_3 == barrier_2:
    barrier_3 = random.randint(0, 35)

barrier_4 = random.randint(0, 35)
while (barrier_4 == start_node or barrier_4 == goal_node or barrier_4 == barrier_1 or barrier_4 == barrier_2
    or barrier_4 == barrier_3):
    barrier_4 = random.randint(0, 35)

# store barriers in a set
barrier_set = set()
barrier_set.add(barrier_1)
barrier_set.add(barrier_2)
barrier_set.add(barrier_3)
barrier_set.add(barrier_4)

def is_valid_move(value, current_node, barrier_set):
    # check if the node in maze
    neighbor_node = maze.find_node(value)
    return (
        0 <= value <= 35 and
        # check if the node is not barrier
        value not in barrier_set and
        # check if the node is in nighbour range
        not ((current_node.x_coordinate == 0 and neighbor_node.x_coordinate == 5) or
             (current_node.x_coordinate == 5 and neighbor_node.x_coordinate == 0))
    )

# print the maze
def print_setup_maze(maze):
    print()
    print('\u001B[35mMaze set up\u001B[39m')
    print()
    current_node = maze.head
    value_count = 1
    while current_node:
        if current_node.value == start_node:
            print('\u001B[34mS    \u001B[39m', end="")
        elif current_node.value == goal_node:
            print('\u001B[34mG    \u001B[39m', end="")
        elif (current_node.value == barrier_1 or current_node.value == barrier_2 or current_node.value == barrier_3 or
              current_node.value == barrier_4):
            print('\u001B[31mB    \u001B[39m', end="")
        else:
            print('.    ', end="")
        if value_count % 6 == 0:
            print('\n')
        value_count += 1
        current_node = current_node.next
    print()