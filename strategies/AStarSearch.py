from strategies.Strategy import Strategy

class AStarSearch(Strategy):

    def __init__(self, heuristic_func=None):
        super().__init__(heuristic_func)
        self.name = "AStarSearch"

    def __call__(self, node):
        return node.depth + self.heuristic_func(node)
