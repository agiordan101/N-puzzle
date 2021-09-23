from strategies.Strategy import Strategy

class DijkstraSearch(Strategy):

    def __init__(self, heuristic_func):
        super().__init__(heuristic_func)
        self.name = "DijkstraSearch"

    def __call__(self, node):
        return 0
