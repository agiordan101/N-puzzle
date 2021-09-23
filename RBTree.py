from Node import Node

BLACK = True
RED = False

class RBTree:

    def __init__(self, root: Node):

        print(f"RBTree init, root=\n{root}heuristic={root.heuristic}")
        self.root = root
        self.root.color = BLACK

    def search(self):
        pass

    # def rotate_right(node, parent: Node, gparent: Node):
    #     pass

    def balance_red_uncle(self, node, parent, gparent, uncle):
        parent.color = BLACK
        uncle.color = BLACK
        gparent.color = RED

    def balance_black_uncle_right_line(self, node, parent, gparent, uncle):
        
        gparent.parent = parent
        gparent.right = parent.left
        parent.left = gparent
        parent.parent = gparent.parent
        parent.color = BLACK
        gparent.color = RED

    def balance_black_uncle_left_line(self, node, parent, gparent, uncle):
        
        gparent.parent = parent
        gparent.left = parent.right
        parent.right = gparent
        parent.parent = gparent.parent
        parent.color = BLACK
        gparent.color = RED

    def balance_black_uncle_left_triangle(self, node, parent, gparent, uncle):
        
        gparent.left = node
        node.left = parent
        node.parent = gparent
        parent.parent = node

    def balance_black_uncle_right_triangle(self, node, parent, gparent, uncle):
        
        gparent.right = node
        node.right = parent
        node.parent = gparent
        parent.parent = node

    def balance_tree(self, node: Node, parent: Node, gparent: Node, uncle: Node):

        if self.root == RED:
            self.root = BLACK
        
        elif uncle and uncle.color == RED:
            self.balance_red_uncle(node, parent, gparent, uncle)

        else:

            if parent.right == node and gparent.right == parent:
                self.balance_black_uncle_right_line(node, parent, gparent, uncle)
            elif parent.left == node and gparent.left == parent:
                self.balance_black_uncle_left_line(node, parent, gparent, uncle)
            
            elif parent.left == node and gparent.right == parent:
                self.balance_black_uncle_left_triangle(node, parent, gparent, uncle)
            else:
                self.balance_black_uncle_right_triangle(node, parent, gparent, uncle)


    def insert(self, node: Node):
        node.color = RED
        parent = None
        current_node = self.root

        # print(f"\nRoot node {self.root}")
        print(f"Insert node {node.heuristic}:\n{node}")

        # SEARCH
        # Go deeper if the child needed exist, in respect of heuristic
        while (current_node.heuristic > node.heuristic and
                current_node.left) or (current_node.right and
                current_node.heuristic < node.heuristic):
            current_node = current_node.left if node.heuristic < current_node.heuristic else current_node.right

        # while current_node.left or current_node.right:
        #     parent = current_node
        #     if current_node.heuristic > node.heuristic:
        #         current_node = current_node.left
        #     else:
        #         current_node = current_node.right

        # INSERT
        node.parent = current_node
        if current_node.heuristic > node.heuristic:
            print(f"Insert left : {node.heuristic} < {current_node.heuristic}")
            current_node.left = node
        else:
            print(f"Insert right : {current_node.heuristic} < {node.heuristic}")
            current_node.right = node

        print(f"current_node :\n{current_node}")
        print(f"current_node parent :\n{current_node.parent}")

        # BALANCE
        gparent = current_node.parent
        if gparent:
            uncle = gparent.left if gparent.right == current_node else gparent.right
            self.balance_tree(node, current_node, gparent, uncle)


    def has_state(self, node: Node):
        pass
