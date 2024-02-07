from MazeProblem.Node import Node


class LinkedList:
  def __init__(self):
    self.head = None

  # insert node to linked list
  def append(self, value, x_coordinate, y_coordinate):
    new_node = Node(value, x_coordinate, y_coordinate)
    if not self.head:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  # check if node is in the linked list
  def find_node(self, value):
    current = self.head
    while current:
      if current.value == value:
        return current
      current = current.next
    return None
