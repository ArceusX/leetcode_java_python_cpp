class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow = ListNode(-1, head)
        fast = head;
        
        while (fast.next):
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
                
        slow.next = slow.next.next
        
        return head

