class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        reverse = 0
        while x:
            reversedN = reversedN * 10 + x % 10
            x //= 10
        if reversedN >= 2 ** 31 - 1 or reversedN <= -2 ** 31:
            return 0
        return -reversedN if isNegative else reversedN
