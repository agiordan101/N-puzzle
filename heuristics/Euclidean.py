from heuristics.Heuristic import Heuristic

class Euclidean(Heuristic):

    def __init__(self, final_state, size):
        super().__init__(final_state, size)
        self.name = 'Euclidean'

    def __call__(self, node):
        self.tmp_state = node.state
        return node.depth + sum([self.compute_euclidean(value) for value in range(self.square_size)])
        # return sum([self.compute_euclidean(value) for value in range(self.square_size)])

    def compute_euclidean(self, value):

        current_index = self.tmp_state.index(value)
        final_index = self.final_state.index(value)
        dx = abs((current_index % self.size) - (final_index % self.size))
        dy = abs((current_index / self.size) - (final_index / self.size))
        return dx * dx + dy * dy