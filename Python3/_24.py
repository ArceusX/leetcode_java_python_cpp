
"""
Algo: We need references to 3 nodes: the 2 we intend to swap
      and the predecessor to the first node to set
      "precedessor.next = second".

      Thus, because head doesn't have a predecessor, we
      create one for it to make the operation on it
      emulate that on every other node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        #Create predecessor to head
        dummy = ListNode(-1, head)

        #Store precedessor's initial node val before it will be overwritten
        predecessor = dummy

        #If last node is "odd" indexed (head as index 1), it is not swapped
        while predecessor.next is not None and predecessor.next.next is not None:

            #Nodes to swap
            first = predecessor.next
            second = predecessor.next.next
            
            #Link swap operations
            predecessor.next = second
            first.next = second.next
            second.next = first

            #Set predecessor to first node of next pair
            predecessor = predecessor.next.next
            
        # "predecessor.next = second" ensures it points to a
        # different head than the one passed into this function.
        return dummy.next
        