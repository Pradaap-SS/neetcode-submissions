# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Step 1: Find the kth node from groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # fewer than k nodes remain, stop

            groupNext = kth.next  # node after the group

            # Step 2: Reverse k nodes
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp       = curr.next
                curr.next = prev
                prev      = curr
                curr      = tmp

            # Step 3: Re-connect with rest of list
            tmp            = groupPrev.next  # old first = new last of group
            groupPrev.next = kth             # connect prev group to new head
            tmp.next       = groupNext       # connect new tail to next group
            groupPrev      = tmp             # move groupPrev to end of reversed group

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr