#Quickest pproach with O(n) time uses hashset

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Convert to set for quick O(1) hashed lookup
        numSet = set(nums)
        longest = 0
        for num in numSet:
            
            #Don't start counting from num whose precedessor is
            #present and with which we can build longer sequence
            if num - 1 not in numSet:
                current = num

                #Increment current end of sequence
                while current + 1 in numSet:
                    current += 1

                #+1 because we also count start num of seq
                longest = max(longest, current - num + 1)

        return longest
        