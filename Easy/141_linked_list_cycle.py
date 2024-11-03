# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = [head]
        while head and head.next is not None:
            if head.next in visited:
                return True
            visited.append(head.next)
            head = head.next

        return False


# heads = [3,2,0,-4]
# pos = 1

# pos_node = None
# for i in range(0, len(heads)):
#     head = ListNode(heads[i])
#     if i == pos:
#         pos_node =

# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
