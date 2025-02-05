from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head.val = None
            return None

        i = 0
        node = head
        while node is not None:
            node = node.next
            i += 1

        node_to_be_delted_index = i - (n - 1)

        if node_to_be_delted_index == 1:
            return head.next

        node = head
        i = 1
        prev = None
        while node is not None:
            if i == node_to_be_delted_index:
                if prev:
                    prev.next = node.next
                node.next = None
            else:
                prev = node
                node = node.next

            i += 1

        return head


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)


print(Solution().removeNthFromEnd(head, 2))
