from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_list = 0
        dummy = ListNode(0, head)
        node = dummy.next
        new_head = None
        while node:
            if not node.next:
                last = node

            len_list += 1
            node = node.next

        k = k % len_list

        curr = dummy
        for _ in range(len_list - k):
            curr = curr.next

        # Now curr is on the new tail
        new_head = curr.next
        curr.next = None
        last.next = head

        return new_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().rotateRight(head, 2))
