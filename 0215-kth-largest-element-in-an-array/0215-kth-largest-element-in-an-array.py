import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        
        res = 0
        
        for _ in range(1, k):
            heapq.heappop(heap)
        
        
        return -heapq.heappop(heap)