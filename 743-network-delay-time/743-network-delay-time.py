from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v,w))
            
        Q = [(0,k)] # (time taken == 0, vertax == k)
        dist = defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q,(alt, v))
        
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1
        
        
        