# 049: Group Anagrams
# Use sorted of chars of str as key to get list to which to 
# add anagram. sorted, being == for anagrams, makes ideal key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    	# If key does not exist, auto insert (key, list)
        d = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            d[sortedS].append(s)

        return [group for group in d.values()]