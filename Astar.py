from heuristics.Euclidean import Euclidean
from Node import Node
from RBTree import RBTree
from AstarData import AstarData

from math import sqrt

import time
# import matplotlib
# matplotlib.use('TkCairo')
# matplotlib.use('MacOSX')
# import matplotlib.pyplot as plt

import plotly.express as px
from plotly.offline import plot

class Astar:

    def __init__(self, initial_state, final_state, search_strategy, beam_search=True):

        print(f"\nASTAR init, strategy: {search_strategy.name}, heuristic: {search_strategy.heuristic_func.name}, beam_search: {beam_search}")
        self.win = False
        self.time_complexity = 0
        self.size_complexity = []
        self.best_heuristic = []
        self.path = None
        self.path_depth = 0

        self.initial_state = initial_state
        self.final_state = final_state
        self.size = int(sqrt(len(initial_state)))
        self.search_strategy = search_strategy

        self.data = AstarData(Node(self.initial_state, search_strategy), beam_search=beam_search)

    def search(self):

        self.search_begin = time.time()
        self.time_complexity = 0
        while self.data.opened and not self.win:

            node = self.data.get_node()
            # print(f"Pop h={node.heuristic}")

            if node.state == self.final_state:
                self.search_end = time.time()
                self.path = node.backward()
                self.path_depth = node.depth
                return self.get_logs()

            for neighbour_state in node.neighbours_state():

                if self.data.is_closed(str(neighbour_state)):
                    continue

                elif self.data.is_open(str(neighbour_state)):
                    self.data.update_opened_node(str(neighbour_state), node)

                else:
                    self.data.open(Node(neighbour_state, self.search_strategy, parent=node))

            self.data.close(node)

            self.time_complexity += 1
            self.size_complexity.append(self.data.get_size_complexity())
            self.best_heuristic.append(node.heuristic)
            if not self.time_complexity % 1000:
                print(f"time_complexity: {self.time_complexity}\t-- size_complexity: {self.size_complexity[-1]}\t-- depth {node.depth}\t-- pop h={node.heuristic}")

        print(f"Can't find a solution.")
        return self.get_logs()

    def get_logs(self):
        return {
            'path': self.path,
            'strategy': self.search_strategy.name,
            'heuristic': self.search_strategy.heuristic_func.name,
            'path_depth': self.path_depth,
            'time_complexity': self.time_complexity,
            'size_complexity': self.size_complexity[-1],
            'time (s)': self.search_end - self.search_begin,
        }

    def print_graph(self):

        # fig, (ax1, ax2) = plt.subplots(1, 2)
        # ax1.plot(range(self.time_complexity), self.size_complexity)
        # ax1.set_title('Size complexity')
        # ax2.plot(range(self.time_complexity), self.best_heuristic)
        # ax2.set_title('Heuristic\'s node open')
        # plt.show()

        # fig = px.scatter(x=range(self.time_complexity), y=self.best_heuristic)
        # fig.update_layout(
        #     title="Astar",
        #     xaxis_title="Time complexity",
        #     yaxis_title="Heuristic\'s node open",
        # )
        # plot(fig)
        
        fig = px.line(x=range(self.time_complexity), y=self.size_complexity, title='Size complexity & heuristic opened over time complexity')
        fig.add_scatter(x=list(range(self.time_complexity)), y=self.best_heuristic)
        # fig.set_title("Astar logs")
        fig.show()