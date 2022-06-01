
"""
Algo: We need access to predecessor to first node in
      pack that will be swapped and successor to pack.
      They are "start" and "end", respectively.

      Head itself will be swapped, so we need to create
      dummy predecessor whose next points to head
"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> Optional[ListNode]:

        #No node given or no swap requested
        if head is None or k == 1:
            return head

        dummy = ListNode(-1, head)

        #Store precedessor's initial node val before it will be overwritten
        predecessor = dummy
        current = head
        count = 0

        while current is not None:
            count += 1

            # If count % k == 0:
            # Arrive at last node of "pack" to reverse. We won't swap/rewire
            # current.next, but we'll rewire next of new final node in
            # pack (that was previously precedessor->current) to point 
            # to current.next (pack's successor). Finally, make new current
            # point to it to prepare for operation on next pack.

            if count % k == 0:
                predecessor = self.reverseList(predecessor, current.next)
                current = predecessor.next

            else:
                # Have not reached last node to swap in pack
                current = current.next

        return dummy.next

    @staticmethod
    def reverseList(start, end):

        # Given list Start -> 1 -> 2 -> 3 -> ... -> End
        # First swap involves 1 and 2 (precedessor and initial current)
        # Store 3 as nextNode = current.next to set up next swap
        # (current.next = start.next) and (start.next = current) wire
        # such that 2 is now placed after S for S -> 2 -> 1 -> 3 -> ...
        # As last step of iteration, proceed to 3.
        # Next swap will place 3 after S for S -> 3 -> 2 -> 1 -> ...

        predecessor = start.next
        current = predecessor.next

        while current is not end:
            nextNode = current.next
            current.next = start.next
            start.next = current
            current = nextNode

        # After swap iterations, wire new final node of pack 1 -> E
        # Return 1 as precedessor to next pack
        predecessor.next = end
        return predecessor
        