from abc import ABCMeta, abstractmethod

class Heuristic(metaclass=ABCMeta):

    def __init__(self, final_state, size):
        self.final_state = final_state
        self.size = size
        self.square_size = size * size

    @abstractmethod
    def __call__(self):
        pass