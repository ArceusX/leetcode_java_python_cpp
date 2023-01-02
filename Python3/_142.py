class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        
        slow = head
        fast = head
        
        hasCycle = False

        while (slow.next and fast.next):
            slow = slow.next
            fast = fast.next
            
            if fast.next:
                fast = fast.next
                
                if slow is fast:
                    hasCycle = True
                    break
                    
        if hasCycle:
        	slow = head

        	while slow is not fast:
        		slow = slow.next
        		fast = fast.next

        	return slow

        else:
        	return None

