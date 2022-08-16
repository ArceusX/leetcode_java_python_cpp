"""
Algo:
For each pack, need access to predecessor to
first node in pack to swap and succcessor to pack

Head itself will be swapped, so create dummy
predecessor whose next points to new head once swapped

For reverse, place current tail before current head as pack
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # No node given or no swap requested
        if not head or k == 1:
            return head

        dummy = ListNode(-1, head)

        # Store initial predecessor before it will be overwritten
        pred = dummy
        tail = head
        count = 0

        while tail:
            count += 1

            # If count % k == 0:
            # Found final node of "pack", now reverse. tail.next
            # won't be rewired but reqire new final node in pack
            # initial pred->next/pack head) to point to tail.next 
            # (pack's successor). Finally, move tail to successor,
            # as first node of next pack

            if count % k == 0:
                pred = self.reverseList(pred, tail.next)
                tail = pred.next

            else:
                # Have not reached last node to swap in pack
                tail = tail.next

        return dummy.next

    @staticmethod
    def reverseList(pred, end):

        # For pack pred -> 1 -> 2 -> 3 -> ... -> end
        # Swap 1 (pred->next) and 2 (tail): store 3 as
        # after = tail.next, place 2 before 1, go to 3
        # Swap 2 and 3 (tail): store 4, place 3 before 2,
        # go to 4. After swaps ifnished, 1 is new final
        # node, wire 1 to point to end, return 1.

        head = pred.next
        tail = head.next

        while tail is not end:
            # Store after as successor to later node to swap
            after = tail.next

            # Wire tail to point to current head of pack
            tail.next = pred.next
            pred.next = tail
            tail = after

        # After swaps, wire new final node of pack (its
        # prev head) as 1 -> end (first node of next pack)
        # Return 1 as precedessor to next pack
        head.next = end
        return head
        