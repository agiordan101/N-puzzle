from heuristics.Manhattan import Manhattan
from heuristics.Euclidean import Euclidean
from heuristics.Sob import Sob
from Astar import Astar
from Node import Node
from Parser import Parser

from Taquin import Taquin

import matplotlib.pyplot as plt
import sys
import argparse

heuristic_func = {
    "euclidean": Euclidean,
    "manhattan": Manhattan,
    "sob": Sob
}


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-heuristic", help="heuristic function", default="euclidean", choices=["euclidean", "manhattan", "sob"])
    arg_parser.add_argument("-file", help="input file here")
    arg_parser.add_argument("-size", type=int, help="board size", default=3)
    args = arg_parser.parse_args()

    parser = Parser(args)

    taquin = Taquin(parser.state)
    if not taquin.is_solvable():
        print("Error: Taquin is not solvable !")
        exit(0)

    astar = Astar(taquin.initial_state, taquin.final_state, heuristic_func=heuristic_func[args.heuristic])
    astar.search()
    
    logs = [astar.get_logs()]
    # astar.print_graph()
    
    print(f"path_depth: {[log['heuristic'] for log in logs]}")
    print(f"path_depth: {[log['path_depth'] for log in logs]}")
    print(f"time_complexity: {[log['time_complexity'] for log in logs]}")
    print(f"size_complexity: {[log['size_complexity'][-1] for log in logs]}")

    # print(f"Path: {logs[0]['path']}")
    
    # subplot(2, 2)
    # lol = []
    # for log in logs:
    #     lol.append(plt.plot(range(log['time_complexity']), log['size_complexity']))
    # plt.legend(handles=[lol[0], lol[1], lol[2]])
    # plt.show()
