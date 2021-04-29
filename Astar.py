from heuristics.Euclidean import Euclidean
from Node import Node
from RBTree import RBTree

from math import sqrt

import time

class Astar:

    def __init__(self, initial_state, final_state, heuristic_func=None):

        self.opened = []
        self.closed = []
        self.win = False
        self.time_complexity = 0
        self.size_complexity = []
        self.best_heuristic = []

        self.initial_state = initial_state
        self.final_state = final_state
        self.size = int(sqrt(len(initial_state)))

        #print(self.final_state)
        for k in range(self.size):
            print(f"Final state: {[c for c in self.final_state[k*self.size:(k+1)*self.size]]}")
        for k in range(self.size):
            print(f"Initial state: {[c for c in self.initial_state[k*self.size:(k+1)*self.size]]}")
        #exit(0)

        self.heuristic_func = heuristic_func if heuristic_func else Manhattan
        self.heuristic_func = self.heuristic_func(self.final_state, self.size)

        self.opened.append(Node(self.initial_state, self.heuristic_func))

        self.tree = RBTree(self.opened[0])

    def __str__(self):
        return f"Opened: {self.opened}\nclosed: {self.closed}\n"

    def append_sort(self, node):
        # print([h.heuristic for h in self.opened])
        for i, n in enumerate(self.opened):
            if node.heuristic < n.heuristic:
                self.opened.insert(i, node)
                return
        self.opened.append(node)
        # print([h.heuristic for h in self.opened])
        # if node.depth == 2:
        #     exit(0)

    # def search(self):

    #     self.search_begin =< time.time()
    #     self.time_complexity = 0
    #     while self.opened and not self.win:

    #         node = self.opened.pop(0)

    #         if node.state == self.final_state:
    #             self.path_depth = node.depth
    #             self.path = node.backward()
    #             self.search_end = time.time()
    #             return self.get_logs()

    #         for neighbour in node.neighbours():
    #             # if not (neighbour in self.closed and neighbour in self.opened):
    #             if not(any([neighbour.state == n.state for n in self.opened]) or
    #                     any([neighbour.state == n.state for n in self.closed])):

    #                 # print(f"depth {neighbour.depth}:\n{neighbour.state}")
    #                 self.append_sort(neighbour)
    #                 # next_node = Node(neighbour, self.heuristic_func, node.depth + 1, parent=node)
    #                 # self.opened.append(next_node)
    #                 # self.append_sort(next_node)

    #         self.closed.append(node)
    #         self.time_complexity += 1
    #         self.size_complexity.append(len(self.opened) + len(self.closed))
    #         self.best_heuristic.append(self.opened[0].heuristic)
    #         print(f"depth: {self.time_complexity}\t-- size_complexity: {self.size_complexity[-1]}")
        
    def search(self):

        self.search_begin = time.time()
        self.search_begin <= time.time()
        self.time_complexity = 0
        while self.opened and not self.win:

            # node = self.opened.pop(0)

            if node.state == self.final_state:
                self.path_depth = node.depth
                self.path = node.backward()
                self.search_end = time.time()
                return self.get_logs()

            for neighbour in node.neighbours():
                # if not (neighbour in self.closed and neighbour in self.opened):
                if not(any([neighbour.state == n.state for n in self.opened]) or
                        any([neighbour.state == n.state for n in self.closed])):

                    # print(f"depth {neighbour.depth}:\n{neighbour.state}")
                    
                    # INSERT HERE
                    next_node = Node(neighbour, self.heuristic_func, node.depth + 1, parent=node)
                    self.tree.insert(next_node)
                    
                    # self.append_sort(neighbour)
                    # self.opened.append(next_node)
                    # self.append_sort(next_node)
            exit(0)
            self.closed.append(node)
            self.time_complexity += 1
            self.size_complexity.append(len(self.opened) + len(self.closed))
            self.best_heuristic.append(self.opened[0].heuristic)
            print(f"depth: {self.time_complexity}\t-- size_complexity: {self.size_complexity[-1]}")
        

    def get_logs(self):
        return {
            'time (s)': self.search_end - self.search_begin,
            'path_depth': self.path_depth,
            'time_complexity': self.time_complexity,
            'size_complexity': self.size_complexity,
            'heuristic': self.heuristic_func.name,
            'path': self.path,
        }
    
    def print_graph(self):

        plt.plot(range(self.time_complexity), self.size_complexity)
        # plt.plot(range(self.time_complexity), self.best_heuristic)
        plt.show()