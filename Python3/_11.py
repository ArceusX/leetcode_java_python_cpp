class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        L, R = 0, len(height) - 1
        
        while L < R:
            shorter = min(height[L], height[R])
            maxArea = max(maxArea, shorter * (R - L))
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
                
        return maxArea
        