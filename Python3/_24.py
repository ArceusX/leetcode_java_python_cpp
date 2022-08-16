"""
Algo: 
Track 3 nodes: ones to swap and predecessor of
1st node for which to set "precedessor.next = second"

Head lacks predecessor, so create one for it so
operation on head emulates that on every other node
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        pred = ListNode(-1, head)

        # Store initial pred(ecessor) before it's overwritten
        dummy = pred

        # If last node is "odd" indexed, it is not swapped
        while pred.next and pred.next.next:

            first = pred.next
            second = pred.next.next
            
            # Wire 1 to point to 2's next, [then] 2 to 1
            pred.next = second
            first.next = second.next
            second.next = first

            # Increment pred to first of next pair
            pred = pred.next.next

        return dummy.next
        