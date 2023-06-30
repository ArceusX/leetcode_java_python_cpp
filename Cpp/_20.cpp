class Solution {
public:
    bool isValid(string s) {
        stack<char> toClose;

        for (char c : s) {

            // open- token: push
            // close-token: this switch, confirm there is close-token
            switch(c) {
                case '(':
                case '{':
                case '[':
                    toClose.push(c);
                    continue;

                case ')':
                case '}':
                case ']':
                    if (toClose.empty()) return false;
            };

            //this switch, now confirm existing close-token matches
            switch(c) {
                case ')':
                    if (toClose.top() != '(') return false;
                    break;

                case '}':
                    if (toClose.top() != '{') return false;
                    break;

                case ']':
                    if (toClose.top() != '[') return false;
                    break;
            }

            toClose.pop();
        }

        // Check all found open-tokens are closed
        return toClose.empty();
    }
};