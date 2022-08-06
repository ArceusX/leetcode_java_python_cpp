class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        if n1 == "0" or n2 == "0": return "0"

        n1Len, n2Len = len(n1), len(n2)

        product = [0] * (n1Len + n2Len)

        for i1 in range(n1Len -1, -1, -1):
            r = n2Len + i1
            for i2 in range(n2Len -1, -1, -1):
                product[r] += int(n1[i1]) * int(n2[i2])
                
                if product[r] > 9:
                    product[r - 1] += product[r] // 10
                    product[r] = product[r] % 10
                    
                r -= 1

        i = 0
        for i in range(len(product)):
            if product[i]:
                break

        return "".join(string.digits[x] for x in product[i:])