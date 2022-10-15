class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(subset, start):
            
            res.append(subset)
            
            for i in range(start,len(nums)):
                dfs(subset + [nums[i]], i + 1)
                
        
        
        dfs([],0)
        
        return res