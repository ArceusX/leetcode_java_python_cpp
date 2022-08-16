class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // sorted ver. -> [unsorted anagram...]
        unordered_map<string, vector<string>> map;
        vector<vector<string>> ret;

        for (const auto& s : strs) {
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            map[sorted].push_back(s);
        }

        ret.reserve(map.size());

        // Push each group of equiv. anagrams into super-group
        for (auto& group : map) {
            // Rather than copy, pass it what would be
            // destroyed anyway after function returns
            ret.push_back(std::move(group.second));
        }
        return ret;
    }
};