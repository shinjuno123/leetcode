class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []
        
        def dfs(elements):
            if not elements:
                res.append(prev[:])
                return
            
            for e in elements:
                c_elements = elements[:]
                c_elements.remove(e)
                prev.append(e)
                dfs(c_elements)
                prev.pop()
                
        
        
        dfs(nums)
        
        return res