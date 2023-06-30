"""
Algo: Keep fast and slow pointers, ++ing fast such fast is n
      steps ahead of slow. When fast reaches tail, slow being
      n steps behind tail, will be nth node before fast | node.
      Remove slow.next by rewiring slow.next = slow.next.next
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # n == 1: remove tail. n < 1: remove non-existent node
        if  n < 1:
            return head

        slow = fast = head
        
        for i in range(0, n):
            if fast.next:
                fast = fast.next

            # Below 2 cases: fast reaches tail before step during
            # which fast, slow moved together. For list of len L,
            # Lth node before tail is head, so [elif case] removes
            # head and return head.next. [else then n > L], would
            # remove non-existent predecessor, so return unchanged
            # # If head is sole node, removing it returns None
            elif i + 1 == n:
                 temp = head.next
                 del head
                 return temp

            else:
                return head

        while fast.next: # Loop until fast reaches tail
              slow = slow.next
              fast = fast.next

        # Only need middle line if unconcerned about memory leaks 
        temp = slow.next
        slow.next = slow.next.next
        del temp

        return head
        