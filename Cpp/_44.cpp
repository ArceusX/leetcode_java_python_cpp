class Solution {
public:
    bool isMatch(string t, string p) {

        int lenT = t.length(), lenP = p.length();

        int iT = 0, iP = 0;

        // Record index to backtrack to
        int indexT = -1, indexP = -1;

        while (iT < lenT) {

            // 1 char match in both p and t
            if ((p[iP] == t[iT]) || p[iP] == '?') {
                iT++, iP++;
            }

            // If find *, record in indexP index after *. Used to backward
            // when need to use * to match. Record index in T with which
            // char after * will next be checked against, it being same iT
            // iT because * can match none in t.
            else if (p[iP] == '*') { 
                indexP = ++iP;
                indexT = iT;
            }

            // No exact or ? match between t and p. Must use *, then need
            // to find match again for char after *. Have checked char
            // after * with char in t recorded together with * (indexT), 
            // now try char after indexT in t

            else if (indexP > -1) { 
                iP = indexP; 
                iT = ++indexT;
            }

            else {
                return false;
            }

        }

        // Once all in t are matched, leftover *'s in p match none at best
        while (p[iP] == '*') {
            iP++;
        }

        // All in p are matched (expended)
        return iP == lenP;
    }
};