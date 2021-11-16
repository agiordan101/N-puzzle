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

from Taquin import Taquin

import sys
import argparse
import json

heuristics = {
    "euclidean": Euclidean,
    "sob": Sob,
    "manhattan": Manhattan
}

strategies = {
    "AStarSearch": AStarSearch,
    "GreedySearch": GreedySearch,
    # "UniformCost": UniformCost,
    # "DijkstraSearch": DijkstraSearch
}

"""
    Open list ->    priority queue & dict[state] = Node
    Close list ->   Just a concatenation of string

    Dijkstra ->     Looking all paths (Based on depth)
    A* ->           Care about path cost and heuristic to open a node

    Greedy search ->Just care about heuristic
    Uniform cost -> Just care about path cost (Cost between nodes are 1, so in this case it's like Dijkstra algorithm)

    beam search ->  Open list length is a fixed value
"""

def solve(taquin, strategy_class, heuristic_class, beam_search, print_path):

    try:
        try:
            heuristic = heuristic_class(taquin.final_state, taquin.size)
            strategy = strategy_class(heuristic)
        except Exception as error:
            print(f"[MAIN ERROR] heuristic or strategy is invalid:\nheuristic={args.heuristic}\tstrategy={args.strategy}\tTraceback:\n{error}")
            exit(0)

        astar = Astar(
            taquin.initial_state,
            taquin.final_state,
            strategy,
            beam_search=beam_search
        )
        logs = astar.search()

        if print_path:
            print(f"path:\n{logs['path']}")

        del logs['path']
        print(f"ASTAR end, logs:\n", json.dumps(logs, indent=4))

        return astar, logs

    except Exception as error:
        print(f"[BENCHMARK ERROR] Astar of heuristic {heuristic.name} has failed:\n{error}")
        exit(0)



if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-heuristic", default="euclidean", choices=heuristics.keys(), help="heuristic function")
    arg_parser.add_argument("-strategy", default="AStarSearch", choices=strategies.keys(), help="strategy function")
    arg_parser.add_argument("-file", help="input file here")
    arg_parser.add_argument("-size", type=int, default=3, help="board size")
    # arg_parser.add_argument("--benchmark", dest='benchmark', action='store_true', default=False, help="benchmark mode (for heuristics)")
    arg_parser.add_argument("--benchmark", dest='benchmark', choices=["heuristics", "strategies"], default=False, help="benchmark mode, for heuristics or strategies")
    arg_parser.add_argument("--path", dest='path', action='store_true', default=False, help="path verbose")
    arg_parser.add_argument("--beam", dest='beam_search', action='store_true', default=False, help="beam search optimization (Affect length of Astar opened list)")
    args = arg_parser.parse_args()

    parser = Parser(args)

    # Generate Taquin
    taquin = Taquin(parser.state, parser.size)
    if not taquin.is_solvable():
        print("\nError: Taquin is not solvable !")
        exit(0)


    if args.benchmark:

        if args.benchmark == "heuristics":
            for name, h_class in heuristics.items():
                solve(taquin, strategies[args.strategy], h_class, args.beam_search, args.path)

        elif args.benchmark == "strategies":
            for name, s_class in strategies.items():
                solve(taquin, s_class, heuristics[args.heuristic], args.beam_search, args.path)

    else:
        astar, logs = solve(taquin, strategies[args.strategy], heuristics[args.heuristic], args.beam_search, args.path)
        print(f"astar.best_heuristics: {astar.best_heuristic}")
        astar.print_graph()
