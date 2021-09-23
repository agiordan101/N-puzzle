from heuristics.Heuristic import Heuristic

class Manhattan(Heuristic):

    def __init__(self, final_state, size):
        super().__init__(final_state, size)
        self.name = 'Manhattan'

    def compute(self, value):

        current_index = self.tmp_state.index(value)
        final_index = self.final_state.index(value)
        return (abs(int(current_index / self.size) - int(final_index / self.size)) +
                abs((current_index % self.size) - (final_index % self.size)))
