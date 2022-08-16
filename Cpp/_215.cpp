/*
Return val for which we have have found (k - 1) vals
larger than it and no other larger. Quicksort until
we find it or sorted entire array
*/

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int lo = 0, hi = nums.size() - 1;
        while (true) {
            int pivot = partition(nums, lo, hi);

            if (pivot == k - 1) return nums[pivot];

            // Case : Fewer than (k - 1) vals exceed pivot
            // Find different pivot in remaining smaller vals
            if (pivot < k - 1) lo = pivot + 1;


            // Case : More than (k - 1) vals exceed pivot
            // Find different pivot in vals exceeding current
            else hi = pivot - 1;
        }
    }

    int partition(vector<int>& nums, int lo, int hi) {
        swap(nums[lo], nums[(lo + hi + 1)/2]);
        int pivI = lo, pivot = nums[pivI];
        lo++;
        while (lo <= hi) {
            if (nums[lo] < pivot && pivot < nums[hi]) {
                swap(nums[lo++], nums[hi--]);
            }
            if (nums[lo] >= pivot) lo++;
            if (nums[hi] <= pivot) hi--;
        }
        swap(nums[pivI], nums[hi]);
        return hi;
    }
};