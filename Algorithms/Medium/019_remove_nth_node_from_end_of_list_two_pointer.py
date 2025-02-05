from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left = dummy_node

        right = head
        while n > 0:
            n = n - 1
            right = right.next

        while right:
            left = left.next
            right = right.next

        # Delete the node after left
        left.next = left.next.next
        return dummy_node.next
