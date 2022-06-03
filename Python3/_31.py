"""
Given a set of digits, its permutations are in lexicographical 
order if value of each permutation is greater than previous's.

Algo: The next (successor) permutation is one that is greater,
(1st) but barely (goal is to minimize how much larger successor is).

      1. Find least-significant (highest index) digit (pivot) 
         that satisfies condition of having a larger digit
         following it. That ensures when swapping, we minimize 
         how much larger permutation will become as result.

      2. Find smallest digit after pivot.

      3. Swap pivot and smallest digit after it (found in step 2)

      4. Sort digits after pivot index from smallest to largest 
         left to right. Thus, we increase least-significant 
         index we can by smallest possible amount, then minimize 
         value of digits after pivot slot by sorting.

Algo: 1. Find highest index i such that s[i] < s[i+1]. If no such
(+)      index exists, permutation is last in set.

      2. Find highest index j > i such that s[j] > s[i]. Such j
         must exist since i+1 suffices if all others fail. s[j] is 
         guaranteed smallest digit for indices after i. If it is 
         not, there is for ii > i, some s[j] > s[ii] > s[i], 
         in which case condition of i in step 1 is violated.

      3. Swap pivot and smallest digit after it (found in step 2)

      4. Reverse all digits with indices greater than i. This 
         suffices to sort them because such digits are in
         decreasing order. If any consecutive pair is not 
         decreasing, condition  of i in step 1 is violated.


      0 1    2  5 3    3  0
      0 1 [P:2] 5 3    3  0
      0 1    2  5 3 [j:3] 0
      0 1   [3] 5 3   [2] 0
      0 1    3  0 2    3  5 (Successor)
"""

class Solution:

    def nextPermutation(self, nums: List[int]):

        n = len(nums)

        index = -1
        # To find highest i satisfying Step 2 condition:
        # Loop backwards to find highest i that fails
        # reversed condition
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break

        # No formal lexigraphical successor, so loop around
        # and return first permutation (lowest order)
        if index == -1:
            reverse(nums, 0, n - 1)
            return

        j = n - 1

        # Step 2: As with Step 1, loop backwards for highest j
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                j = i
                break

        # Step 3
        nums[index], nums[j] = nums[j], nums[index]

        # Step 4: Reverse elems with indices > i
        reverse(nums, index + 1, n - 1)
    
def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1