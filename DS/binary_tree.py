class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ,")
        if self.right:
            self.right.print_tree()

    def in_order_traverse(self, root: "Node"):
        """
        Inorder traversal
        Left -> Root -> Right
        """
        result: list = []
        if root:
            result = self.in_order_traverse(root.left)
            result.append(root.data)
            result += self.in_order_traverse(root.right)

        return result

    def pre_order_traverse(self, root: "Node"):
        """
        Preorder traversal
        Root -> Left ->Right
        """
        result: list[int] = []

        if root:
            result.append(root.data)
            result += self.post_order_traverse(root.left)
            result += self.post_order_traverse(root.right)

        return result

    def post_order_traverse(self, root: "Node"):
        """
        Postorder traversal
        Left ->Right -> Root
        """
        result: list[int] = []
        if root:
            result += self.post_order_traverse(root.left)
            result += self.post_order_traverse(root.right)
            result.append(root.data)

        return result


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.post_order_traverse(root))
