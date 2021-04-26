from heuristics.Heuristic import Heuristic
from heuristics.Manhattan import Manhattan
from heuristics.Euclidean import Euclidean

from math import sqrt

class Sob(Heuristic):

    def __init__(self, final_state, size):
        # super().__init__(final_state, size)
        self.euclidean = Euclidean(final_state, size)
        self.manhattan = Manhattan(final_state, size)
        self.name = 'Sob'

    def __call__(self, node):
        return node.depth + (self.euclidean(node) + self.manhattan(node)) / 2
        