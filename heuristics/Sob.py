from heuristics.Heuristic import Heuristic
from heuristics.Manhattan import Manhattan
from heuristics.Euclidean import Euclidean

class Sob(Heuristic):

    def __init__(self, final_state, size):
        super().__init__(final_state, size)
        self.euclidean = Euclidean(final_state, size)
        self.manhattan = Manhattan(final_state, size)
        self.name = 'Sob'

    def __call__(self, node):
        self.euclidean.tmp_state = node.state
        self.manhattan.tmp_state = node.state
        return sum([self.compute(value) for value in range(self.square_size)])

    def compute(self, value):
        return (self.euclidean.compute(value) + self.manhattan.compute(value)) / 2
