# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next   # save next before overwriting
            curr.next = prev   # reverse the pointer
            prev = curr        # move prev forward
            curr = next        # move curr forward

        return prev
        