# 002: Add Two Numbers (Digits Being Nodes in Linked List)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0

        # falseHead: Base holding result digits, but to
        #            be excluded from result
        falseHead = ListNode(-1)
        current   = falseHead
        
        while (l1 or l2):
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = sum // 10

            # Add latest result digit (exclude carry)
            current.next = ListNode(sum % 10)

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry != 0:
            current.next = ListNode(carry)
            
        return falseHead.next
        