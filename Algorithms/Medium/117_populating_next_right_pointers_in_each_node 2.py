from collections import deque, defaultdict


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None
        bfs_result: defaultdict = self.level_order_with_levels(root)

        for level, nodes in bfs_result.items():
            for j in range(len(nodes)):
                if j == len(nodes) - 1:
                    nodes[j].next = None
                else:
                    nodes[j].next = nodes[j + 1]

        return root

    def level_order_with_levels(self, root: Node) -> dict:
        if not root:
            return []

        queue = deque([(root, 0)])
        result = defaultdict(list)

        while queue:
            current, level = queue.popleft()
            result[level].append(current)

            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))

        return result
