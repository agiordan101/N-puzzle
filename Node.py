from math import sqrt

class Node:

    def __init__(self, state, search_strategy, parent=None):

        # self.color = None
        # self.left = None    #Red black tree
        # self.right = None   #Red black tree

        self.state = state
        self.state_id = str(state)
        self.state_id_len = len(self.state_id)
        self.size = int(sqrt(len(state)))
        self.search_strategy = search_strategy
        self(parent)

    def __call__(self, parent):
        # node.depth is acting like cost function, c(n) = depth
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0 # Depth is different than time_complexity
        self.heuristic = self.search_strategy(self)

    def __str__(self):
        return ''.join([f"{['-' if c == 0 else c for c in self.state[k*self.size:(k+1)*self.size]]}\n" for k in range(self.size)])


    def hash(self):
        return str(self.state)

    def neighbours_state(self):

        index = self.state.index(0)
        y, x = index / self.size, index % self.size
        neighbours = [
           (x - 1 >= 0, -1),
           (x + 1 < self.size, +1),
           (y - 1 >= 0, -self.size),
           (y + 1 < self.size, +self.size),
        ]
        for exist, di in neighbours:
            if exist:
                state = self.state.copy()
                state[index] = state[index + di]
                state[index + di] = 0
                # yield Node(state, self.heuristic_func, self)
                yield state
    
    def backward(self, log=""):
        if self.parent:
            return self.parent.backward(str(self) + '\n' + log)
        else:
            return str(self) + '\n' + log
