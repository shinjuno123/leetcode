class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        
        
        
        def dfs(elements,index,k):
            
            if k == 0:
                res.append(elements)
                return
            
            for i in range(index,n + 1):
                dfs( elements + [i],i+1, k - 1)
        
        
        
        
        dfs([],1,k)
        
        
        return res
        
        