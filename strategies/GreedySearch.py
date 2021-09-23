from strategies.Strategy import Strategy

class GreedySearch(Strategy):

    def __init__(self, heuristic_func=None):
        super().__init__(heuristic_func)
        self.name = "GreedySearch"

    def __call__(self, node):
        return self.heuristic_func(node)
