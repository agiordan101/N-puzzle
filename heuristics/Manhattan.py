from heuristics.Heuristic import Heuristic

class Manhattan(Heuristic):

    def __init__(self, final_state, size):
        super().__init__(final_state, size)
        self.name = 'Manhattan'

    def __call__(self, node):
        # score = 0
        # self.tmp_state = node.state
        # for value in square_size:
        #     score += self.compute_manhattan(value)
        # return score
        self.tmp_state = node.state
        return node.depth + sum([self.compute_manhattan(value) for value in range(self.square_size)])

    def compute_manhattan(self, value):

        current_index = self.tmp_state.index(value)
        final_index = self.final_state.index(value)

        return abs((current_index / self.size) - (final_index / self.size)) + abs((current_index % self.size) - (final_index % self.size))