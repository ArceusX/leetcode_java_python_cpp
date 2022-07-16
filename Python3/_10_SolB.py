class Solution(object):
    def isMatch(self, t: str, p: str) -> bool:

        lenT, lenP = (len(t), len(p))
        
        # while iP < lenP: (explained)
        # After iteration iP (encompassing chars of p[:iP+1])
        # arr[x] is True if p[ :iP+1] and t[ :x] match exactly
        # After iteration lenP - 1, arr[lenT] gives result
        # of match check between p[ :lenP] and t[ :lenT],
        # or match check between complete t and p

        arr = [False for iT in range(lenT + 1)]

        # Before any iteration/iteration -1, arr[0] = True 
        # because p = "" and t = "" (both empty) should match
        arr[0] = True
        
        iP = 0
        while iP < lenP:

            # If find _*: Check which char (or none) in t
            # satisfies match with "_*"
            if iP < (lenP - 1) and p[iP + 1] == "*":

                # Slide "_*" in p and compare to chars of t
                # = arr[iT + 1]: Allow * match zero char, which it can
                # = arr[iT] and (p[iP] == t[iT] or p[iP] == "."):
                #   Current result extends from previous result with
                #   current check, of either exact p[iP] == t[iT] or . 
                for iT in range(lenT):
                    arr[iT + 1] = arr[iT + 1] or \
                    (arr[iT] and (p[iP] == t[iT] or p[iP] == "."))

                # "_*" is 2-token pattern, consumed together, so shift 2
                iP += 2

            # * wildcard match any 1 char: each result extends from
            # previous result (shift arr right 1), but arr[0] == False
            # because * cannot match none (empty) t, so prepend [False]
            elif p[iP] == ".":
                arr = [False] + arr[:-1]
                iP += 1

            # Exact char p[iP]: Shift right, but with check condition
            else:

                # Check p[iP] against each char in t, looping backward
                # to base each current result on previous result
                # between t[ :iT] and previous iteration's p substring
                for iT in range(lenT - 1, -1, -1):
                    arr[iT + 1] = arr[iT] and (t[iT] == p[iP])

                # Exact char in p cannot match none (ie t: ""/empty)
                arr[0] = False
                iP += 1

        return arr[lenT]