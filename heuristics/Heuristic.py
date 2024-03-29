from abc import ABCMeta, abstractmethod

class Heuristic(metaclass=ABCMeta):

    def __init__(self, final_state, size):
        self.final_state = final_state
        self.size = size
        self.square_size = size * size

    def __call__(self, node):
        self.tmp_state = node.state
        self.last_heuristic = sum(self.compute(value) for value in range(self.square_size))
        return self.last_heuristic

    @abstractmethod
    def compute(self):
        pass
