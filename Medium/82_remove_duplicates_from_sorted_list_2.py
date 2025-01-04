from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        deummy = ListNode(0, next=head)
        node = deummy
        prev = deummy
        while node:
            if node.next and node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next

                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next

        return deummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)


print(Solution().deleteDuplicates(head))
