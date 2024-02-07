from MazeProblem.LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    # check if the stack is empty
    def is_empty(self):
        return self.linked_list.head is None

    # push nodes to the stack
    def push(self, value, x_coordinate, y_coordinate):
        self.linked_list.append(value, x_coordinate, y_coordinate)

    # remove top
    def pop(self):
        if self.is_empty():
            return None
        current = self.linked_list.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.linked_list.head = None
        return current

    # view the top
    def peek(self):
        if self.is_empty():
            return None
        current = self.linked_list.head
        while current.next:
            current = current.next
        return current
