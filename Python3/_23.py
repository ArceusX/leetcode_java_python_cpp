"""
Algo: 
Allot remaining lists (initially all: 0 to len(lists) - 1)
to scan between two merge tasks, which will allot between 
their own sub-tasks, until a task needs to merge only two lists. 

Indices (start, end) track each lists are alloted to each task.
"""

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        return self.mergeLists(lists, 0, len(lists) - 1)

    def mergeLists(self, lists, start, end):

        # Only one list remains for task, so no need to merge
        if start == end:
            return lists[start]

        # Allot lists between two merge tasks, which
        # will further allot until an task is alloted
        # only two lists whose entries it can sort by "riffle shuffle"

        mid = (start + end) // 2

        left = self.mergeLists(lists, start, mid)
        right = self.mergeLists(lists, mid + 1, end)

        return self.merge(left, right)

    @staticmethod
    def merge(left, right):

        # Dummy node whose next points to would-be smallest of merged list
        head = ListNode(-1)
        tail = head

        while left and right:

            #Append smaller val node to tail, then shift along list of appended node
            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next

            #Shift tail along for next append
            tail = tail.next

        # Append remaining of one or no remaining list
        if left:
            tail.next = left

        if right:
            tail.next = right


        return head.next
        