class Solution {
    public int[] nextPermutation(int[] nums) {
        
        int n = nums.length;

        int index = -1;

        for (int i = n - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                index = i - 1;
                break;
            }
        }

        if (index == -1) {
            reverse(nums, 0, n - 1);
            return nums;
        }
        int j = n - 1;

        for (int i = n - 1; i >= index + 1; i--) {
            if (nums[i] > nums[index]) {
                j = i;
                break;
            }
        }
        
        int temp = nums[index];
        nums[index] = nums[j];
        nums[j] = temp;

        reverse(nums, index + 1, n - 1);
        
        return nums;
    }

    private static void reverse(int[] nums, int i, int j) {
        while (i < j) {
            
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            
            i++;
            j--;
        }
    }
}