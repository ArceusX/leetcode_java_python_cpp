class Solution {
public:
    // t is text/haystack; p is pattern/needle to search for
    string minWindow(string t, string p) {

        // Each iteration, either ++ iTStart or iTEnd
        int iTStart = 0, iTEnd = 0, minStart = 0, nToFind = p.size(), minLen = INT_MAX;
        
        // Modify to record # of copies of char in P we still
        // need to find in T. Negative val marks more copies
        // found in T for current window than necessary for P
        unordered_map<int, int> toFind;
        for (char c : p) toFind[c]++;

        while (iTEnd < t.size()) {

            // If char of T matches char in P with copies to find, 
            // nToFind-- to mark 1 fewer copy to find. If we
            // don't need to find another copy, char's toFind 
            // count will be negative, permitting us to remove it 
            // in current window of T and still keep valid window
            if ((toFind[t[iTEnd]]--) > 0) {
                nToFind--;
            }
            iTEnd++;

            // If all in P found, anchor iTEnd, test how 
            // much forward iTStart can be shifted before 
            // losing found chars in P 
            while (nToFind == 0) {

                // Check if minLen window needs to be updated
                if (iTEnd - iTStart < minLen) {
                    minLen = iTEnd - iTStart;
                    minStart = iTStart;
                }

                // Only if count in P eactly matches count in
                // window of T, will removing it makes window
                // no longer valid (toFind[t[iTStart]] == 0)
                // If losing char at iTStart loses necessary
                // copy, mark we must exit loop, return to 
                // outer loop to ++iTEnd and try to regain it

                if (toFind[t[iTStart]]++ == 0) nToFind++;
                iTStart++;
            }
        }
        return minLen != INT_MAX ? t.substr(minStart, minLen) : "";
    }
};