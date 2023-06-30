# 2080: Get Count of Target Value Between L, R Array Indices

# Complexity: O(n) space, O(ln n) time 
# Group indices in arr holding same value, each group being
# naturally sorted, and map group to value. Get group from
# key target and return length = bisect_right - bisect_left, 
# where right is 1 + index of R and left is index of L in group

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.found = defaultdict(list)

        for i, val in enumerate(arr):
            self.found[val].append(i)
        
    def query(self, L: int, R: int, target: int) -> int:
        v = self.found[target]

        # bisect_left:      leftmost  index in V with value L
        # bisect_right: 1 + rightmost index in V with value R
        # Get index after, but not, final holding target value
        # If none in V exceeds R, bisect_right() gives len(found)
        return bisect.bisect_right(v, R) - bisect.bisect_left(v, L)