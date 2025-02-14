from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        node1 = dummy1
        node2 = dummy2

        node = head
        while node:
            if node.val >= x:
                node2.next = node
                node2 = node2.next
            else:
                node1.next = node
                node1 = node1.next

            node = node.next

        node1.next = dummy2.next
        node2.next = None
        return dummy1.next


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)


print(Solution().partition(head, 3))
