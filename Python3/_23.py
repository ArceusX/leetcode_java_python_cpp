# Class that wraps ListNode and defines comparison for heapq use
class ComparableNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        merged = falseHead = ListNode(-1)

        # if node: Consider only non-None nodes
        leaders = [ComparableNode(node) for node in lists if node]

        # If no non-None node in lists, there is nothing to merge
        if not leaders:
            return None

        # With heap, get least among current traversed node of each list 
        heapq.heapify(leaders)

        while len(leaders) > 1: # while comparison is still needed
            least       = heapq.heappop(leaders)
            merged.next = least.node
            merged      = merged.next

            # Upon adding least to merged, shift to next of that least
            if least.node.next:
                heapq.heappush(leaders, \
                ComparableNode(least.node.next))

        merged.next = heapq.heappop(leaders).node # Add remaining list

        return falseHead.next