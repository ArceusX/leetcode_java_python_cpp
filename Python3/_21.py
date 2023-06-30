class Solution:
    def mergeTwoLists(self, curr1: Optional[ListNode], curr2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = l1, l2

        # Create 2 ptrs: tail onto which nodes merge, 
        # falseHead that points to eventual head of merged
        tail = falseHead = ListNode(-1)

        while curr1 and curr2:
        	if  curr1.val < curr2.val:
        		tail.next = curr1
        		curr1 = curr1.next

        	else:
        		tail.next = curr2
        		curr2 = curr2.next

        	tail = tail.next

        # After either list depleted: end comparison, 
        # other remains, merge its current tracked 
        if curr1: tail.next = curr1
        if curr2: tail.next = curr2

        return falseHead.next
