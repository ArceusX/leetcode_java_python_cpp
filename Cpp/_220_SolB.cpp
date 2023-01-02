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
public:

    long getBucketIndex(int higher, long min, long capacity) {
        return ((long) higher - min) / capacity;
    }

    bool containsNearbyAlmostDuplicate(vector<int>& nums, int diffId, int diffVal) {
        unordered_map<long, long> buckets;

        long min = *min_element(nums.begin(), nums.end());

        long capacity = (long) diffVal + 1;

        for (int i = 0; i < nums.size(); i++) {
            long index = getBucketIndex(nums[i], min, capacity);

            if (buckets.count(index)) return true;

            if (buckets.count(index - 1) && 
                nums[i] - buckets[index - 1] < capacity) {
                return true;
            }

            if (buckets.count(index + 1) && 
                buckets[index + 1] - nums[i] < capacity) {
                return true;
            }

            buckets.emplace(index, (long) nums[i]);

            if (i >= diffId) {
                buckets.erase(getBucketIndex(nums[i - diffId], min, capacity));
            }
        }
        return false;
    }
};

