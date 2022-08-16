class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        priority_queue<pair<int, int>> queue;
        unordered_map<int, int> freqMap;
        vector<int> ret;
        ret.reserve(k);

        for (int e : nums) freqMap[e]++;

        for (auto freq : freqMap) {
            queue.push({ freq.second, freq.first });
        }

        while (k--) {
            ret.push_back(queue.top().second);
            queue.pop();
        }
        return ret;
    }
};