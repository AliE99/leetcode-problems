# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev




def print_list(node):
    while node is not None:
        print(f" {node.val}", end="")
        node = node.next
    print()


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


print("Given Linked list:", end="")
print_list(head)

new_head = Solution().reverseList(head)
print("Result Linked list:", end="")
print_list(new_head)