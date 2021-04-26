from heuristics.Manhattan import Manhattan
from heuristics.Euclidean import Euclidean
from heuristics.Sob import Sob
from Astar import Astar
from Node import Node

import matplotlib.pyplot as plt

if __name__ == "__main__":

    # initial_state = [13, 12, 4, 1, 3, 11, 14, 10, 15, 7, 2, 0, 8, 6, 5, 9]
    initial_state = [2, 5, 0, 7, 4, 8, 6, 1, 3]

    heuristics = [Sob, Manhattan, Euclidean]
    # heuristics = [Manhattan]
    # heuristics = [Euclidean]
    # heuristics = [Sob]
    logs = []
    for heuristic in heuristics:
        astar = Astar(initial_state, heuristic_func=heuristic)
        astar.search()
        logs.append(astar.get_logs())
        # astar.print_graph()
        # print(logs)
    
    print(f"path_depth: {[log['heuristic'] for log in logs]}")
    print(f"path_depth: {[log['path_depth'] for log in logs]}")
    print(f"time_complexity: {[log['time_complexity'] for log in logs]}")
    print(f"size_complexity: {[log['size_complexity'][-1] for log in logs]}")
    
    # subplot(2, 2)
    # lol = []
    # for log in logs:
    #     lol.append(plt.plot(range(log['time_complexity']), log['size_complexity']))
    # plt.legend(handles=[lol[0], lol[1], lol[2]])
    # plt.show()
