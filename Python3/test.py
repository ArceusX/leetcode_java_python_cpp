class Solution(object):
    def isMatch_B(self, t: str, p: str) -> bool:

        lenT, lenP = (len(t), len(p))
        arr = [False for iT in range(lenT + 1)]
        arr[0] = True
        
        iP = 0

        for iP in range(lenP):
            if p[iP] == "*":
                for iT in range(lenT):
                    arr[iT + 1] = arr[iT + 1] or arr[iT];

            elif p[iP] == ".":
                arr = [False] + arr[:-1]

            else:

                for iT in range(lenT - 1, -1, -1):
                    arr[iT + 1] = arr[iT] and (t[iT] == p[iP])

                arr[0] = False

        return arr[lenT]