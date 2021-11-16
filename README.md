# N-puzzle

The goal of this project is to solve the n-puzzle ("taquin" in French) game using the A* search algorithm or one of its variants.

- 'Parser' object helps for parsing and cleaning data
- 'Taquin' object simulates the n-puzzle game.

  
- 'AStar' object is a modular A* algorithm witch can works with some of its variants and different Heuristics functions.
    
        Heuristics used in A* algoritm to evaluate a game board (All are a sum of distances between each square and its final position):
        
        - Manhattan distances
        - Euclidean distances
        - Euclidean distances miness a constant if a square is arrived in the right position.

        "Strategies" used in A* are the way to use heuristics value and actual depth of the algorithm (Variant of A*):
        
        - Uniform cost:         Just care about path cost (Cost between nodes are 1, so in this case it's like Dijkstra algorithm)
        - Dijkstra algorithm:   Looking all paths (Based on depth)
        - Greedy Search:        Just care about heuristic
        - Classic AStar:        Care about path cost and heuristic to open a node

  
- 'Node' object are used in 'AstarData' to saved data of A*.
- 'AstarData' object is an optimized data structure for A*.
    
        Open list is simulate with a priority queue of 'Node' and a dictionnary of 'Node' based on the state.
        - "beam search" optimization is also available (Open list has a fixed length)
        Closed list is simulate with a 'str' object, who represent a concatenation of all 'Node'.state_id
