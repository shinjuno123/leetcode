class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(elements, start):
            
            res.append(elements)
            
            for i in range(start,len(nums)):
                dfs(elements + [nums[i]],i + 1)
        
        dfs([],0)
        
        return res