# 024: Swap Nodes in Pairs

# Sol 1
# If nodes' val can be swapped, swap vals rather than rewire next ptrs
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        back = head
        lead = back.next

        while lead:
            back.val, lead.val = lead.val, back.val

            # Next pair: shift back 2, set lead to node after back 
            back = lead.next
            lead = back.next if back else None

        return head


# Sol 2: Under restriction only next ptrs, and not vals, can change
# Track 3 nodes: pred(ecessor) whose next rewiring; back: rewire its
# next to point to lead.next; lead: follows back before swap
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        falseHead = ListNode(-1, head)
        pred      = falseHead
        back      = head
        lead      = back.next

        while lead:
            # lead replaces back as node pointed to by pred
            pred.next = lead

            # Set back to point to 1st node in next pair (before swap)
            back.next = lead.next

            # before: back -> lead. now: lead -> back
            lead.next = back

            # pred for next iter: back because back took lead's place
            pred = back

            # After rewire, now move back to 1st node in next pair
            back = back.next

            # Move lead to back's successor to ready for next iter
            lead = back.next if back else None

        return falseHead.next