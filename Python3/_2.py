# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0

        # False head: we'll be actually returning result.next
        result = ListNode(-1)
        pointer = result
        
        while (l1 or l2):
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = sum // 10

            # Add next node of ones digit. Then move to it
            pointer.next = ListNode(sum % 10)
            pointer = pointer.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if (carry):
            pointer.next = ListNode(carry)
            
        return result.next
        