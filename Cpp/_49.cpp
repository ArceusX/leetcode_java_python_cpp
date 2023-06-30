// 049: Group Anagrams
// Use sorted of chars of str as key to get list to which to 
// add anagram. sorted, being == for anagrams, makes ideal key

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // new sorted equiv -> [unsorted equivs in strs]
        unordered_map<string, vector<string>> map;

        for (const auto& s : strs) {
            string sorted = s;
            sort(sorted.begin(), sorted.end());

            // if key sorted doesn't exist, auto assign it list
            map[sorted].push_back(s);
        }

        vector<vector<string>> groups;
        groups.reserve(map.size());

        // Push each group of anagrams into groups
        for (auto& [i, group] : map) {

            // Rather than copy group, pass original that
            // would be destroyed anyway upon function return
            groups.push_back(std::move(group));
        }
        return groups;
    }
};