class Solution:
    def reverse(self, x: int) -> int:
        
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
            
        reverse = 0
        while (x != 0):
            leastSig = x % 10
            # if reverse > (2^31 - 1) // 10 or
            # reverse == (2^31 - 1) // 10 and (leastSig > 2^31 - 1) % 10
            # If isNegative, max allowed for abs(x) is 2^31 instead
            if (reverse > 214748364) or \
            (reverse == 214748364 and leastSig > (7 + isNegative)):
                return 0

            reverse = reverse * 10 + leastSig
            x //= 10

        return -reverse if isNegative else reverse