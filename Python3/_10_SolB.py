class Solution(object):
    def isMatch(self, t: str, p: str) -> bool:

        lenT, lenP = (len(t), len(p))
        
        # while iP < lenP:
        # Upon iteration iP (encompassing chars of p[:iP+1])
        # arr[x] == True if p[ :iP+1] and t[ :x] match exactly
        # Upon iteration lenP - 1, arr[lenT] gives result
        # of match between p[ :lenP] and t[ :lenT]

        arr = [False for iT in range(lenT + 1)]

        # Before any iteration/at iP == -1, arr[0] == True 
        # because p = "" and t = "" (both empty) should match
        arr[0] = True
        
        iP = 0
        while iP < lenP:

            # If find _*: Check which char (or none) in t
            # satisfies match with "_*"
            if iP < (lenP - 1) and p[iP + 1] == "*":

                # Compare "_*" in p and successive chars of t
                # = arr[iT + 1]: Allow * match zero char, which it can
                # = arr[iT] and (p[iP] == t[iT] or p[iP] == "."):
                #   Extend from result of previous checks and current
                #   check of either exact p[iP] == t[iT] or . wildcard 
                for iT in range(lenT):
                    arr[iT + 1] = arr[iT + 1] or \
                    (arr[iT] and (p[iP] == t[iT] or p[iP] == "."))

                # "_*" consumes two paired tokens of p, so shift 2
                iP += 2

            # * must match any 1 char: each result extends from exact
            # predecessor (shift arr >> 1), but * cannot match
            # none (empty) t, so prepend [False] so arr[0] == False
            elif p[iP] == ".":
                arr = [False] + arr[:-1]
                iP += 1

            # For p[iP] != "." or not preceding "*": Check 1 char match
            else:

                # Check p[iP] against each char in t, looping backward
                # to base each current result on previous result
                # between t[ :iT] and p substring on previous iters
                for iT in range(lenT - 1, -1, -1):
                    arr[iT + 1] = arr[iT] and (t[iT] == p[iP])

                # Iter 0 or after, exact char in p cannot match empty t
                arr[0] = False
                iP += 1

        return arr[lenT]