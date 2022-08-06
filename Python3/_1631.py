"""
Djikstra: Starting with fromNode [0, 0], calculate cost to fromNode's 
          cardinal nbors via relax func (abs difference of fromNode's
          val and nbor's val). If newly calculated cost is less than
          current min cost for that nbor, update nbor's min cost and
          add that cost and nbor's coordinates to heap. Next iter,
          set fromNode to min result popped from heap. If fromNode
          destination node, return its cost
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nRows, nCols = len(heights), len(heights[0])
        costs = [[float('inf')] * nCols for _ in range(nRows)]
        costs[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            cost, row, col = heapq.heappop(heap)
            if (row == nRows - 1) and (col == nCols - 1):
                return cost

            for r, c in (row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col):
                if (0 <= r < nRows) and (0 <= c < nCols):
                    toCost = max(cost, abs(heights[r][c] - heights[row][col]))

                    if toCost < costs[r][c]:
                        costs[r][c] = toCost
                        heapq.heappush(heap, (toCost, r, c))