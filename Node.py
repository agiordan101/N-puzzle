from math import sqrt

class Node:

    state = []
    heuristic = None
    parent = None
    # childs = None

    def __init__(self, state, depth, heuristic_func):

        self.state = state
        self.depth = depth
        self.heuristic_func = heuristic_func
        self.size = int(sqrt(len(state)))

    def __call__(self):
        if self.heuristic is None:
            self.heuristic = self.heuristic_func()
        return self.heuristic

    def __str__(self):
        return ''.join([f"{['-' if c == 0 else c for c in self.state[k*self.size:(k+1)*self.size]]}\n" for k in range(self.size)])

    def hash(self):
        return str(self.state)

    def neighbours(self):
        # [('0' et 'x'), ...]
        # list comprehension dessus
        neighbours = []
        index = self.state.index('0')
        y, x = index / self.size, index % self.size

        if x - 1 >= 0:
            move = self.state[:index] + self.state[index-1] + self.state[index+1:]
            neighbours.append(move[:index-1] + '0' + move[index:])
        if x + 1 < self.size:
            move = self.state[:index] + self.state[index+1] + self.state[index+1:]
            neighbours.append(move[:index+1] + '0' + move[index+2:])

        if y - 1 >= 0:
            move = self.state[:index] + self.state[index-self.size] + self.state[index+1:]
            neighbours.append(move[:index-self.size] + '0' + move[index-self.size+1:])
        if y + 1 < self.size:
            move = self.state[:index] + self.state[index+self.size] + self.state[index+1:]
            neighbours.append(move[:index+self.size] + '0' + move[index+self.size+1:])

        return neighbours
    
    def backward(self, log=""):
        if parent:
            return parent.backward(log + "\n" + str(self))