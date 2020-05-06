"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.


-1 Restate the problem
    - take the binary numbers from linked list, convert to base 10

-2 Ask clarifying questions
    -can i use int()

-3 State your assumptions
    - I can use int()
    - head is at 0

-4 Think out loud
  -4a Brainstorm solutions
        - return val of each node, convert, return
  -4b Explain your rationale
        - each node can only be 1 or 0, if i traverse and return each value and append them to a list or string, i can just do the conversion regularly
  -4c Discuss tradeoffs
        - 
  -4d Suggest improvements
        - 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ll = ""
        while head:
            ll = ll + str(head.val)
            head = head.next

        return int(ll, 2)
