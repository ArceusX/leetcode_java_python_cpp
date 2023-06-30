# Hard: Unmastered. Uses dynamic programming

"""
. = matches any single char
* = matches zero or more of (guaranteed existing) preceding char

Text and pattern must match exactly.

Algo    : Calculate result as result of earlier checks (memoized in
          table) and current chars check. Return highest-indices
          entry of table as result over full text and full pattern.

Complexity
Time    : O(lenT * lenP) for text T, pattern p

          Iterate over each char of pattern p and check if it matches
          each char of t. Outer loop of lenP, inner loop of lenT

Space   : O(m * n)

          We keep array indexing result matching each char 
          of t of size m and each of p of size n.
"""

class Solution:
    def isMatch(self, t: str, p: str) -> bool:
        
        lenT, lenP = (len(t), len(p))
        
        # Add 1 more row and 1 more col because other checks
        # need to be able to reference check of t of empty str
        # and p of empty str, which must give result True.
        arr = [[False for iT in range(lenT + 1)] for iP in range(lenP + 1)]
        arr[0][0] = True;

        # *, guaranteed preceded by alphanumeric, permits zero match
        # of alphanumeric, allowing * and preceeding alphanumeric
        # to be ignored (e.g. result of [iP - 2] -> result of [iP])
        # IE, if p = "" matches t = "", "a*" also matches ""
        # arr[0][0] = True lets us match "" with p: "_*", "_*_*", etc

        for iP in range(2, lenP + 1):
            if p[iP - 1] == '*':
                arr[iP][0] = arr[iP - 2][0]

        for iP in range(1, lenP + 1):    
            for iT in range(1, lenT + 1):
                # . is wildcard (matches any 1)
                # p[iP - 1] == t[iT - 1]: edges for strings line up
                # = arr[iP - 1][iT - 1], result of check equals 
                # result of check with previous edges
                if p[iP - 1] == '.' or p[iP - 1] == t[iT - 1]:
                    arr[iP][iT] = arr[iP - 1][iT - 1]

                # Unnecessary to check iP > 1, because prcecusor
                # guaranteed for * (* guaranteed to not be 0th char)
                elif p[iP - 1] == '*':

                    # From * as p[iP-1], check p[iP-2], for any . before *
                    # Or if preceding x in 'x*' matches an 'x' in t
                    # If either True, indicate . or x in t matches x in p.
                    # Slide edge of t left 1 to check for more matches
                    # of x in t (property of *). Edge of p remains at x.
                    if p[iP - 2] == '.' or p[iP - 2] == t[iT - 1]:
                        arr[iP][iT] = arr[iP][iT - 1]

                    # Either there's match (above if), so we use that, 
                    # or permitted no match, so borrow result of char 
                    # preceding "_*". arr[iP-2][iT] exists because we created 
                    # column for t of "".
                    arr[iP][iT] = arr[iP][iT] or arr[iP - 2][iT]

        return arr[lenP][lenT]

