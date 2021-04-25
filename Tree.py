from Node import Node
from heuristics import manhattan

class Tree:

    tree = {}
    opened = []
    closed = []
    
    def __init__(self, inital_state, heuristic_func=manhattan):

        self.heuristic_func = heuristic_func
        
        self.initial_node = Node(inital_state, 0, heuristic_func)
        # print(str(self.initial_node))
        # exit(0)
        self.open([self.initial_node])

    def __str__(self):
        return f"Opened: {self.opened}\nclosed: {self.closed}\ntree: {self.tree}"

    def open(self, neighbours):
        # List of Node

        for neighbour in neighbours:
            self.tree[neighbour.hash()] = neighbour
            self.opened.append(neighbour)
    """
    def open(self, node):

        for neighbour in node.neighbours():
            if not neighbour in self.tree:
                neighbour_node = Node(neighbour, node.depth + 1)
                self.tree[neighbour] = neighbour_node
                self.opened.append(neighbour_node)
    """
    def close(self, node):
        pass

