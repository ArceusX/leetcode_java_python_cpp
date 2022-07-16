class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        // Unordered_set (backed by hashtable) for quick O(1) average lookup
        unordered_set<string> dict(wordList.begin(), wordList.end());
        
        if (dict.find(endWord) == dict.end()) {
            return 0;
        }

        // Bidirectional search halves distance (d) from start to goal, which
        // is applied exponentially to average # of neighbors (b)
        // Thus, time O(b^d) -> 2 * O(b^(d/2)).
        // Each iteration, current smaller set will be treated as lookSet
        // and assigned to *pLook, and lookSet's entries checked for match
        // against entries of checkSet. Neighbors of look entries will be
        // added to lookSet. Potential swap of roles next iteration.

        unordered_set<string> lookSet = {beginWord}, checkSet = {endWord}, *pLook = &lookSet, *pCheck;

        //Guaranteed beginWord != endWord, so dist is min 2 if path exists
        int dist = 2;

        while (!pLook->empty()) {

            if (lookSet.size() < checkSet.size()) {
                pLook = &lookSet;
                pCheck = &checkSet;
            } else {
                pLook = &checkSet;
                pCheck = &lookSet;
            }

            unordered_set<string> newLookSet;
            for (auto it = pLook -> begin(); it != pLook -> end(); it++) {
                string word = *it;

                // Check whether looked-at word with 1 char changed matches any
                // goal word in checkSet. If not, but that new word appears in
                // dict, mark it to look up or check against on next iteration.
                for (int i = 0; i < word.size(); i++) {

                    // Allows return to original word for next modification
                    char prevC = word[i];

                    for (int j = 0; j < 26; j++) {
                        word[i] = 'a' + j;
                        if (pCheck -> find(word) != pCheck -> end()) {
                            return dist;
                        }
                        if (dict.find(word) != dict.end()) {
                            newLookSet.insert(word);
                            dict.erase(word);
                        }
                    }
                    word[i] = prevC;
                }
            }
            dist++;
            
            //Remove prev entries in newLookSet iterated over, add their neighbors
            *pLook = newLookSet;
        }
        return 0;
    }
};