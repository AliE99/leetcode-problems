from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        right_node = after_right_node = None

        i = 1
        node = head
        while node is not None:
            if i == right:
                right_node = node
                after_right_node = node.next

            node = node.next
            i += 1

        i = 1
        node = head
        while node is not None:
            if i == left - 1:
                next = node.next
                node.next = right_node
                node = next

            elif i == left:
                prev = node
                next = node.next
                node.next = after_right_node
                node = next

            elif i > left and i <= right:
                next = node.next
                node.next = prev
                prev = node
                node = next
            else:
                node = node.next
            i = i + 1

        if left == 1:
            return prev
        return head


head = ListNode(3)
head.next = ListNode(5)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

print(Solution().reverseBetween(head, 1, 2))