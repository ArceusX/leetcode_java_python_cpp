"""
Algo: Keep pointers fast and slow, incrementing fast n steps
      ahead of slow. When fast reaches tail, slow will be
      n steps behind tail and slow.next nth node from end.
      Remove slow.next by rewiring slow.next = slow.next.next
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        
        for i in range(0, n):
            fast = fast.next

        # If fast reaches end before moving pointers together
        # For list of length L, Lth node before end is head
        # If reach end after ++ fast n times, nth node before
        # end is head or head's predecessor
        # To do: remove head, return head.next
        # If head is sole node, removing node will return None
        if not fast:
            return head.next

        # Loop until fast reaches tail, if it hasn't already
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove previous slow.next
        slow.next = slow.next.next

        return head
        