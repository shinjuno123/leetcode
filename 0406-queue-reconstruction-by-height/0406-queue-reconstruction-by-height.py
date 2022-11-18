import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        
        for person in people:
            heapq.heappush(heap, (-person[0],person[1]))
        
        result = []
        
        while heap:
            height, index = heapq.heappop(heap)
            result.insert(index,[-height, index])
        
        return result