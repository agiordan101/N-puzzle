from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):

    def __init__(self, heuristic_func=None):
        self.heuristic_func = heuristic_func

    @abstractmethod
    def __call__(self, node):
        pass
