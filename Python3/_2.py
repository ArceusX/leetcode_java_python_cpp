# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = ListNode(0)
        pointer = result
        
        while (l1 or l2):
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            sum_digit = sum % 10
            carry = sum // 10
            
            pointer.next = ListNode(sum_digit)
            pointer = pointer.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if (carry != 0):
            pointer.next = ListNode(carry)
            
        return result.next
        