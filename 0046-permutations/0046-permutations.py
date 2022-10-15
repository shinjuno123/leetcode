class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []
        
        def dfs(elements):
            if not elements:
                res.append(prev[:])
                return
            
            for e in elements:
                current_elem = elements[:]
                current_elem.remove(e)
                prev.append(e)
                dfs(current_elem)
                prev.pop()
        
        
        dfs(nums)
        
        
        return res