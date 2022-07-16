class Solution:
    def isMatch(self, t: str, p: str) -> bool:

        lenT, lenP = (len(t), len(p))

        # Record index to backtrack to in "while edgeP < finalStarP + 1:"
        indexP = -1
        indexT = -1

        # finalStarP tracks index of final * in t and finalStarT
        # its line-upped index in p, counting backward.
        # Once initialized (from -1), they won't be changed later
        finalStarP = -1
        finalStarT = -1

        # Find first * while checking if any char in t that is not
        # * or ? fails to match with the same index char in p,
        # which signals a forward non-match between t and p
        for i in range(lenP):
            if p[i] == '*':
                indexP = indexT = i
                break

            # Only * can match more than 1 char. If no * were found
            # and lenT <= i < lenP, p cannot match enough (all) of t
            elif lenT <= i:
                return False

            # For not p[i] == t[i], previous elif ensures i has not
            # moved past len(t) - 1
            elif not (p[i] == '?' or p[i] == t[i]):
                return False
            
        # No * in p, if no char failed match (previous elif) and
        # checked every in both t and p: return True
        if indexP == -1:
            return lenT == lenP
        
        # Iterate from ends of t, p, searching for final * in p
        # and matching it to line-upped index in t, backward
        for ir in range(1, lenP + 1):
            if p[lenP - ir] == '*':
                finalStarP = lenP - ir
                finalStarT = lenT - ir
                break

            # Match backward with ends line-upped. No * to complicate
            elif not(p[lenP - ir] == '?' or t[lenT - ir] == p[lenP - ir]):
                return False

            # indexT == # of chars before first * in p. At least ir chars 
            # after final * (final * may be first *). Elif True: 
            # Even if all *'s match zero chars, will be more chars in p
            # than are available in t to match them
            elif lenT < indexT + ir:
                return False
        
        # s contains only 1 * and both forward and backward checks pass
        if indexP == finalStarP:
            return True
 
        # t: "mississippi"
        # p: "m??*ss*?i*pi"

        # Set edge of p to char after first *. Only use * to match when needed,
        # for which we'll move edgeP, edgeT back for matchs again (see else)
        edgeT = indexT
        indexP += 1
        edgeP = indexP

        # For each non-* char in p, ensure exists char in t between char
        # immediately after first * to final * (inclusive) that can match it
        while edgeP < finalStarP + 1:

            # * can match none, so don't move edge of t forward. indexT for else:
            # If ever need to use *, need match again for char after it (indexP)
            if p[edgeP] == '*':
                indexT = edgeT
                edgeP += 1
                indexP = edgeP

            # Elif True: To find match for 1-char-match char in p, would need
            # to search match in t beyond finalStarT, but all chars after
            # finalStarT have already been used for match, so return fail
            elif finalStarT < edgeT:
                return False

            # For match with exact char or ?, move both edges forward.
            # Edges may be moved back if we must use * to match
            elif p[edgeP] == '?' or p[edgeP] == t[edgeT]:
                edgeT += 1
                edgeP += 1

            # If no match for edge in t with exact or ? in p, must try * match,           
            # for which we move edge of p back to char after previous * to check
            # again with lowest-index char in t that hasn't been checked against
            # it (having already checked it against indexT, now try indexT += 1)
            # If that lowest-index unchecked char in t fails, try next one
            else:
                edgeP = indexP
                indexT += 1
                edgeT = indexT
        
        return True