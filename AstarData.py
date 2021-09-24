class AstarData:

    def __init__(self, node, beam_search=False):

        self.open = self.beam_search_open if beam_search else self.just_open
        self.opened = {node.state_id: node}
        self.opened_sort = [node]
        self.closed = []
        self.closedstr = "

    def get_node(self):
        del self.opened[self.opened_sort[0].state_id]
        return self.opened_sort.pop(0)

    def beam_search_open(self, node):
        if len(self.opened_sort) < 500:
            self.just_open(node)
        else:
            if node.heuristic < self.opened_sort[-1].heuristic:
                self.just_open(node)
                del self.opened[self.opened_sort[-1].state_id]
                del self.opened_sort[-1]

    def just_open(self, node):
        self.opened[node.state_id] = node
        for i, n in enumerate(self.opened_sort):
            if node.heuristic < n.heuristic:
                self.opened_sort.insert(i, node)
                return
        self.opened_sort.append(node)

    def is_open(self, state_id):
        return state_id in self.opened.keys()

    def update_opened_node(self, state_id, parent):
        if self.opened[state_id].depth > parent.depth + 1:
            # print(f"Update node depth {self.opened[state_id].depth} to {parent.depth + 1}")
            self.opened[state_id](parent)

    def close(self, node):
        self.closed.append(node.state_id)

    def is_closed(self, state_id):
        return state_id in self.closed
"""
    def close(self, node):
        self.closedstr += node.state_id
       
    def is_closed(self, state_id):
        return self.closedstr.find(state_id) != -1
"""
    
    
    
    
    
    
