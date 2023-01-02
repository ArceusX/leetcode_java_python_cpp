/*
Majority Voting Algo:

Initialize nums[0] as candidate elem and its count to 1.
Everytime we encounter elem of same val as candidate,
count++. If encounter different val to candidate, 
count-- and update candidate to that new val.

At end, check that count of candidate indeed is
half or more of total votes/size of nums
*/


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0];
        int nCandidate = 0;
        
        for (const int& num : nums) {
            if (num == candidate) nCandidate++;
            else {
                nCandidate--;
                if (--nCandidate == 0) {
                    nCandidate = 1;
                    candidate = num;
                }
            }
        }
        
        return candidate;
    }
};