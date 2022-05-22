"""
Complexity
Time      : O(m x n) for s of size m, p of size n,

            We iterate over each char of pattern p 
            and check if it matches each char of s.
            Thus, loop of range m nested in loop of range n

Space     : O(m x n)

            We keep array indexing each char of
            s of size m and each of p of size n,
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        sizeS, sizeP = (len(s), len(p))
        
        # Add 1 more row and 1 more col because we need to have
        # other checks reference check of s of empty str and
        # p of empty str, which must give result True
        arr = [[False for j in range(sizeP + 1)] for i in range(sizeS + 1)]
        arr[0][0] = True;

        # *, always preceded by alphanumeric, can match none
        # of preceding alphanumeric, thus allowing * and
        # that alphanumeric to be ignored (e.g. [i - 2] -> i)
        # IE, if p = "" matches s = "", "a*" also matches ""
        # arr[0][0] = True lets us match "" with "_*"

        for j in range(2, sizeP + 1):
            if p[j - 1] == '*':
                arr[0][j] = arr[0][j - 2]

        for i in range(1, sizeS + 1):
            for j in range(1, sizeP + 1):

                # . is wildcard (matches any 1)
                # s[i - 1] == p[j - 1]: edges for strings line up
                # = arr[i - 1][j - 1], result of check equals 
                # result of check with previous edges
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    arr[i][j] = arr[i - 1][j - 1]

                #Unnecessary to check j > 1, because * is guaranteed
                #to have precursor (* guaranteed to not ever be 0th char)
                elif p[j - 1] == '*':

                    # After * as p[j-1], check p[j-2], for any . before *
                    # Or if preceding x in 'x*' matches an 'x' in s
                    # If either True, indicate x in s matches x in p.
                    # Slide edge in s left 1 to check for more matches
                    # of x in s (property of *)
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        arr[i][j] = arr[i - 1][j]

                    # * permits none match, so borrow result corresponding
                    # to char preceding "_*", even if no
                    # such p[j-2]
                    arr[i][j] = arr[i][j] or arr[i][j - 2]

        return arr[sizeS][sizeP]

