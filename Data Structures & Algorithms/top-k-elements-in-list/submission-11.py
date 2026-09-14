from collections import defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        minheap = []

        for num in nums:
            freq[num]+=1
        for num, count in freq.items():
            heapq.heappush(minheap, (count, num))
            if len(minheap) >k:
                heapq.heappop(minheap)

        return [num for count, num in minheap]

