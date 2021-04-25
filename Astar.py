from Tree import Tree
from heuristics import manhattan
from math import sqrt

class Astar:

    def __init__(self, initial_state, heuristic_func=manhattan):

        self.size = int(sqrt(len(initial_state)))
        self.initial_state = initial_state
        self.final_state = [0 for i in range(self.size * self.size)]
        self.compute_final_state()

        self.tree = Tree(self.initial_state, heuristic_func)

    def compute_final_state(self):

        x, y = 0, 0
        n = self.size
        #print(self.size)
        value = 1
        while value < self.size * self.size:
            i = 0
            while i < n:
                #print(f"{value}: index {i} - coords y/x {y}/{x}")
                self.final_state[x + y * self.size] = value
                value += 1
                i += 1
                x += 1
            
            x -= 1
            y +=1
            n -= 1

            i = 0
            while i < n:
                #print(f"{value}: coords y/x {y}/{x}")
                self.final_state[x + y * self.size] = value
                value += 1
                i += 1
                y += 1
            if value == self.size * self.size:
                break

            x -= 1
            y -= 1
            
            i = 0
            while i < n:
                #print(f"{value}: coords y/x {y}/{x}")
                self.final_state[x + y * self.size] = value
                value += 1
                i += 1
                x -= 1

            x += 1
            y -= 1
            
            n -= 1

            i = 0
            while i < n:
                #print(f"{value}: coords y/x {y}/{x}")
                self.final_state[x + y * self.size] = value
                value += 1
                i += 1
                y -= 1
            x += 1
            y += 1
        
        for k in range(self.size):
            print(f"Final state: {[c for c in self.final_state[k*self.size:(k+1)*self.size]]}\n")
        # print(self.final_state)

    def search():

        while self.tree.opened and not self.win:

            node = self.tree.opened.pop(0)

            if node.state == self.final_state:
                return node.backward()

            # if not node in self.tree:
            # neighbour_node = Node(neighbour, node.depth + 1)
            
        
