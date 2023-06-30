# 206: Reverse linked list
# Track 3 pointers: back; lead: back.next before swap;
# nextLead: record lead.next before swap. Make lead
# point to back, shift back and lead up for next iter.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        back = head
        lead = back.next

        while lead: # If lead, guarantees back is non-None
            # Record before rewiring would overwrite this data
            nextLead = lead.next

            lead.next = back
            back, lead = lead, nextLead # lead takes role of next back

        head.next = None

        # "while lead" exited on back that is tail of original
        # list (ie next == None). Put it as head of reversed list
        return back 