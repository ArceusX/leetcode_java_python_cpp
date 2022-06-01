"""
Algo: Maintain two nodes, fast and slow, with fast being n steps
      ahead of slow. When fast reaches the end of the list,
      where slow is then at will be n steps from end.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        slow = head
        fast = head
        
        #After each iteration, i gives # of steps fast is ahead of slow
        for i in range(0, n):

            if fast.next is None:

                # (i == n - 1) implies we've reach tail, so end would be
                # nth node, and thus, the node n steps before it is head

                if i == n - 1:
                    head = head.next

                return head

            fast = fast.next

        # Loop until fast node reaches to the end
        # Now we will move both slow and fast pointers
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        #If slow is tail (ie n = 1), slow.next would be null
        if slow.next is not None:
            slow.next = slow.next.next

        return head
        