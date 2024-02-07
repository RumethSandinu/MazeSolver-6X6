class Node:
    def __init__(self, value, x_coordinate, y_coordinate):
        self.value = value
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.next = None
        self.parent = None
        self.cost = 0
        self.heuristic_cost = 0
