class Solution {
public int longestConsecutive(int[] nums) {
    Set<Integer> set = new HashSet<>();
    
    int maxLen = 0;
    for (int num : nums) {
        set.add(num);
    }
    
    for (int num: nums) {

        // If num has not been accounted for by subsequence 
        // it belongs to
        if (set.contains(num) == false) continue;

        // Check if set contains num - 1, then 1 less of that
        // and so on, removing those nums we account for
        // Need to make copy of num because we use original num 
        // to start computing the "count-up" subsequence
        int lower = num - 1;
        while (set.contains(lower)) {
            set.remove(lower);
            lower--;
        }
        
        // Use num
        num++;
        while (set.contains(num)) {
            set.remove(num);
            num++;
        }
        maxLen = Math.max(maxLen, num - lower - 1);
    }
    return maxLen;
}
}