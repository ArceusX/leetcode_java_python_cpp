/*
For entry in []nums, interpret its index as inNode and its
val as outNode. Duplicate val is one that has two inEdges:
start of cycle. Problem reduces to that of finding start
*/

public class Solution {
    public int findDuplicate(int[] nums) {

        // Given []nums contains vals from [1, nums.len]
        // 0 has no inEdge and thus it suffices as head
        // of corresponding linked list

        int slow = 0; 
        int fast = 0;

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } 
        while (slow != fast);

        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;
    }
}