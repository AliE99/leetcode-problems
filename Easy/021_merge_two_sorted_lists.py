# Definition for singly-linked list.
from typing import Optional
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.linked_list import create_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining elements of list1 or list2
        current.next = list1 if list1 else list2

        return dummy.next


l1 = [1, 2, 4]
linked_list1 = create_linked_list(l1)

l2 = [1, 3, 4]
linked_list2 = create_linked_list(l2)

result = Solution().mergeTwoLists(list1=linked_list1, list2=linked_list2)
print(result)
