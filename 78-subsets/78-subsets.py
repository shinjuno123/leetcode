class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        k = len(nums)
        
        def dfs(elements,start):
            
            results.append(elements.copy())
        
            
            for i in range(start,k):
                dfs(elements + [nums[i]],i+1)
        
        
        dfs([],0)
        
        return results