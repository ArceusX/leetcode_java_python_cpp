class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        size_t maxLen = std::max_element(wordDict.begin(), wordDict.end(),
        	[](const auto& w1, const auto& w2) {return w1.size() < w2.size();})->size();

        int sLen = s.size();
        vector<bool> isValid(sLen + 1, false);
        isValid[0] = true;

        for (int i = 1; i <= sLen; i++) {
        	for (int j = i - 1; j >= 0 && maxLen >= (i - j); j--) {

                if (isValid[j] && (std::find(wordDict.begin(), wordDict.end(), 
        			s.substr(j, i - j)) != wordDict.end())) {
                        isValid[i] = true;
                        break;
                    }
        	}
        }

        return isValid[sLen];
    }
};