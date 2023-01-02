/*
Bucket Approach

Rather than compare specific vals, flag bucket (each holding capacity
of diffVal + 1; bucket holds up to bucket's min + diffVal, inclusive)
each val belongs to and record val. For current val, if its bucket
is flagged/already filled or either neighbor buckets is filled and
filling vals for neighbor buckets is within diffVal of current val,
return True. Each iteration, unflag bucket for nums[i - diffId]
*/

class Solution {
    private long getBucketIndex(int higher, int min, long capacity) {
        return ((long) higher - (long) min) / capacity;
    }
    public boolean containsNearbyAlmostDuplicate(int[] nums, int diffId, int diffVal) {
        Map<Long, Long> buckets = new HashMap<>();

        int min = Integer.MAX_VALUE;
        for (int num : nums) min = Math.min(num, min);

        long capacity = (long) diffVal + 1;

        for (int i = 0; i < nums.length; i++) {
            long index = getBucketIndex(nums[i], min, capacity);

            if (buckets.containsKey(index)) return true;

            if (buckets.containsKey(index - 1) && 
                nums[i] - buckets.get(index - 1) < capacity) {
                return true;
            }

            if (buckets.containsKey(index + 1) && 
                buckets.get(index + 1) - nums[i] < capacity) {
                return true;
            }

            buckets.put(index, (long) nums[i]);
            if (i >= diffId) {
                buckets.remove(getBucketIndex(nums[i - diffId], min, capacity));
            }
        }
        return false;
    }
}