# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        number1 = self.extract_number(node=l1)
        number2 = self.extract_number(node=l2)
        number3 = number1 + number2
        node = None
        for num in str(number3):
            node = ListNode(val=int(num), next=node)

        return node

    def extract_number(self, node: ListNode) -> int:
        number: str = ""
        while node is not None:
            number = f"{node.val}{number}"
            node = node.next
        return int(number)


# Function to create a linked list from a list
def create_linked_list(arr):
    if not arr:  # if the list is empty, return None
        return None

    head = ListNode(arr[0])  # create the head of the linked list
    current = head

    for value in arr[1:]:  # iterate over the rest of the values
        current.next = ListNode(value)  # create a new node and link it
        current = current.next  # move to the next node

    return head


l1 = [2, 4, 3]
linked_list1 = create_linked_list(l1)

l2 = [5, 6, 4]
linked_list2 = create_linked_list(l2)

print(Solution().addTwoNumbers(linked_list1, linked_list2))
