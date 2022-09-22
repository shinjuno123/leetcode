class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        prev = []
        
        def dfs(elements,start,k):
            
            if k == 0:
                results.append(prev.copy())
                return
            
            for i in range(start, n+1):
                prev.append(i)
                dfs(prev, i+1, k-1)
                prev.pop()
        
        dfs([],1,k)
        
        return results