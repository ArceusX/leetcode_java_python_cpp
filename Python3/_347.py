class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        d = defaultdict(int)
        heap = []
        re = []

        for num in nums:
        	d[num] += 1

        for (num, freq) in d.items():
        	heapq.heappush(heap, (-freq, num))

        for _ in range(k):
        	re.append(heapq.heappop(heap)[1])

        return re



