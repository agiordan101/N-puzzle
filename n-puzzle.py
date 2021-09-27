from strategies.DijkstraSearch import DijkstraSearch
from strategies.UniformCost import UniformCost
from strategies.GreedySearch import GreedySearch
from strategies.AStarSearch import AStarSearch
from heuristics.Manhattan import Manhattan
from heuristics.Euclidean import Euclidean
from heuristics.Sob import Sob
from Astar import Astar
from Node import Node
from Parser import Parser
from RBTree import RBTree

from Taquin import Taquin

import sys
import argparse

heuristics = {
    "euclidean": Euclidean,
    "manhattan": Manhattan,
    "sob": Sob
}

strategies = {
    "DijkstraSearch": DijkstraSearch,
    "UniformCost": UniformCost,
    "GreedySearch": GreedySearch,
    "AStarSearch": AStarSearch
}

"""
    Open list ->    priority queue & dict[state] = Node
    Close list ->   Just a list
                    Try with 10-tree

    Dijkstra ->     Looking all paths
    A* ->           Care about path cost and heuristic to open a node

    Greedy search ->Just care about heuristic
    uniform cost -> Just care about path cost

    beam search ->  Open list length is 500
"""

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-heuristic", help="heuristic function", default="euclidean", choices=heuristics.keys())
    arg_parser.add_argument("-strategy", help="strategy function", default="AStarSearch", choices=strategies.keys())
    arg_parser.add_argument("-file", help="input file here")
    arg_parser.add_argument("-size", type=int, help="board size", default=3)
    args = arg_parser.parse_args()

    parser = Parser(args)
    print(parser.state)

    taquin = Taquin(parser.state)
    if not taquin.is_solvable():
        print("Error: Taquin is not solvable !")
        exit(0)

    class_heuristic = heuristics[args.heuristic]
    print(f"class_heuristic: {class_heuristic}")
    heuristic = class_heuristic(taquin.final_state, parser.size)
    # heuristic = heuristics[args.heuristic](taquin.final_state, parser.size)
    search_strategy = strategies[args.strategy](heuristic)
    logs = []
    n_astar = 1
    for i in range(n_astar):
        astar = Astar(
            taquin.initial_state,
            taquin.final_state,
            search_strategy,
            beam_search=False
        )
        astar.search()

        logs.append(astar.get_logs())
        # astar.print_graph()

        # print(logs[-1])

    # print(f"Path:\n{logs[0]['path']}")

    print(f"Average of {n_astar} astar")
    print(f"time (s): {sum([log['time (s)'] for log in logs]) / n_astar}")
    print(f"path_depth: {sum([log['path_depth'] for log in logs]) / n_astar}")
    print(f"time_complexity: {sum([log['time_complexity'] for log in logs]) / n_astar}")
    print(f"size_complexity: {sum([log['size_complexity'][-1] for log in logs]) / n_astar}")

    
    # subplot(2, 2)
    # lol = []
    # for log in logs:
    #     lol.append(plt.plot(range(log['time_complexity']), log['size_complexity']))
    # plt.legend(handles=[lol[0], lol[1], lol[2]])
    # plt.show()
