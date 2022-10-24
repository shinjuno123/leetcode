class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, elements, k):
            if k == 0:
                res.append(elements)
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(i + 1, [] + elements, k - 1)
                elements.pop()
            
        
        dfs(1,[],k)
        
        return res