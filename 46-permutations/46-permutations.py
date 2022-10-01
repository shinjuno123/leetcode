class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev = []
        res = []
        
        
        
        def dfs(elements):
            
            if len(elements) == 0:
                res.append(prev[:])
                return
            
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev.append(e)
                dfs(next_elements)
                prev.pop()
        
        
        dfs(nums)
        
        
        return res
        