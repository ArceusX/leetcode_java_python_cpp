# 007: Reverse Integer
# If reversed would go out of [-2^31, 2^31 - 1] range, return 0 instead

class Solution:
    def reverse(self, x: int) -> int:

        # Unlike in C++, in Py, (a mod n) returns + result even
        # for a < 0 and n < 0. Thus, in Py, extract - sign and add
        # it back separately. Py: -6 % -10 == -6; C++: -6 % -10 == 6
        isNegative = False
        if x < 0:
            # Will convert to 1 to resolve - range is 1 wider than + range
            isNeg = True
            x = -x
            
        reverse  = 0
        while (x > 0):
            leastSig = x % 10
            # if reverse  > (2^31 - 1) // 10 or
            #    reverse == (2^31 - 1) // 10 and (leastSig > 2^31 - 1) % 10
            # Highest allowed final digit of (+|-) is (7|8)
            if (reverse  > 214748364) or \
               (reverse == 214748364 and leastSig > (7 + isNeg)):
                return 0

            reverse = reverse * 10 + leastSig
            x //= 10

        return -reverse if isNeg else reverse