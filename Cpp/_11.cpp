/* Standard std library functions included
   so unnecessary to include <include algorithm>
   or using namespace std; */

class Solution {
public:
    int maxArea(vector<int>& height) {

        int max_width = height.size();
        
        int left = 0;
        int right = max_width - 1;
        int max_area = 0;
        
        while (left < right) {
            int shorter_height = (height[left] < height[right]) ? height[left] : height[right];
            max_area = max(max_area, shorter_height * (right - left));
            
            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return max_area;
    }
};