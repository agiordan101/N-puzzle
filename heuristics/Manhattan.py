from heuristics.Heuristic import Heuristic

class Manhattan(Heuristic):

    def __init__(self, final_state, size):
        super().__init__(final_state, size)
        self.name = 'Manhattan'

    def compute(self, value):

        current_index = self.tmp_state.index(value)
        final_index = self.final_state.index(value)
        dx = abs((current_index % self.size) - (final_index % self.size))
        dy = abs(int(current_index / self.size) - int(final_index / self.size))
        return dx + dy
