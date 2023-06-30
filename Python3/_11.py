# 011: Container With Most Water
# Start with max width (bounds at left- and right- most)
# Each iter, --width (move shorter bound by height inward)
# Stop iteration when bounds touch

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        L, R = 0, len(height) - 1
        
        while L < R:
            shorter = min(height[L], height[R])
            maxArea = max(maxArea, shorter * (R - L))
 
            # Move shorter bound inward           
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
                
        return maxArea
        