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
        bfs_result = self.bfs(root)
        i = 1
        while bfs_result:
            temp: list[Node] = bfs_result[:i]
            for j in range(len(temp)):
                if j == len(temp) - 1:
                    temp[j].next = None
                else:
                    temp[j].next = temp[j + 1]

            bfs_result = bfs_result[i:]
            i *= 2

        return root

    def bfs(self, root: Node) -> list:
        if root is None:
            return []

        # Level-order traversal: use a queue
        result = []
        queue = deque([root])

        while queue:
            current = queue.popleft()
            result.append(current.val)

            # Add left and right children to the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result


def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is not None:
            temp = Node(val=arr[i])
            root = temp

            # insert left child
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


# arr = [1, 2, 3, 4, 5, None, 7]
arr = [1, 2, None, 3, None, 4, None, 5]


root = None
root = insert_level_order(arr, root, 0, len(arr))

print(Solution().connect(root))
