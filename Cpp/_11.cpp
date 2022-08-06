class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int maxArea = 0;
        int L = 0, R = height.size() - 1;
        
        while (L < R) {
            int shorter = (height[L] < height[R]) ? height[L] : height[R];
            maxArea = max(maxArea, shorter * (R - L));
            
            if (height[L] < height[R]) L++;
            else R--;
        }
        return maxArea;
    }
};