from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        mp = {None: None}
        node = head
        while node is not None:
            copy: Node = Node(x=node.val)
            mp[node] = copy
            node = node.next

        node = head
        while node is not None:
            copy_node: Node = mp[node]
            copy_node.next = mp[node.next]
            copy_node.random = mp[node.random]
            node = node.next

        return mp[head]
