class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set(nums)
        _maxLen = 0
        for num in nums:
            _len = 1;
            _lower = num - 1;
            
            while (_lower in _set):
                _set.remove(_lower)
                _lower -= 1
                _len += 1
                
            num += 1
            while (num in _set):
                _set.remove(num)
                num += 1
                _len += 1
                
            _maxLen = max(_maxLen, _len)
            
        return _maxLen
    