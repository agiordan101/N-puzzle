BLACK = True
RED = False

class RBTree:


    def __init__(self, root):
        self.root = root
        self.root.color = BLACK

    def search(self):
        pass

    def rotate_right(node, parent, gparent):
        pass

    def balance_red_uncle(node, parent, gparent, uncle):
        parent.color = BLACK
        uncle.color = BLACK
        gparent.color = RED

    def balance_black_uncle_right_line(node, parent, gparent, uncle):
        
        gparent.parent = parent
        gparent.right = parent.left
        parent.left = gparent
        parent.parent = gparent.parent
        parent.color = BLACK
        gparent.color = RED

    def balance_black_uncle_left_line(node, parent, gparent, uncle):
        
        gparent.parent = parent
        gparent.left = parent.right
        parent.right = gparent
        parent.parent = gparent.parent
        parent.color = BLACK
        gparent.color = RED

    def balance_black_uncle_left_triangle(node, parent, gparent, uncle):
        
        gparent.left = node
        node.left = parent
        node.parent = gparent
        parent.parent = node

    def balance_black_uncle_right_triangle(node, parent, gparent, uncle):
        
        gparent.right = node
        node.right = parent
        node.parent = gparent
        parent.parent = node

    def balance_tree(self, node, parent, gparent, uncle):

        if self.root == RED:
            self.root = BLACK
        
        elif uncle.color == RED:
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


    def insert(self, node):
        node.color = RED
        current_node = self.root

        while current_node.left or current_node.right:

            if current_node.heuristic > node.heuristic:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node.heuristic > node.heuristic:
            current_node.left = node
        else:
            current_node.right = node
            
        gparent = current_node.parent
        uncle = gparent.left if gparent.right == current_node else gparent.right
        self.balance_tree(node, current_node, gparent, uncle)