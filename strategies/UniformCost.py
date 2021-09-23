from strategies.Strategy import Strategy

class UniformCost(Strategy):

    def __init__(self, heuristic_func=None):
        super().__init__(heuristic_func)
        self.name = "UniformCost"

    def __call__(self, node):
        return node.depth
