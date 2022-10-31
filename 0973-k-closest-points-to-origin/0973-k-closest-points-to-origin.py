import heapq
class Solution:
    @staticmethod
    def get_euclidean_distance(x1, x2):
        return x1**2 + x2 ** 2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            heapq.heappush(heap,[self.get_euclidean_distance(point[0],point[1])] + point)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1:])
            
        
        return res
        