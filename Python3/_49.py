class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list);
        ret = []

        for s in strs:
            leader = ''.join(sorted(s))
            d[leader].append(s)

        for group in d.values():
            ret.append(group)

        return ret