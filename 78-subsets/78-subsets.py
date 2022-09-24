class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        k = len(nums)
        
        def dfs(elements,start):
            
            results.append(elements.copy())
            
            if len(elements) == k:
                return
            
            for i in range(start,k):
                elements.append(nums[i])
                dfs(elements,i+1)
                elements.pop()
        
        
        dfs([],0)
        
        return results