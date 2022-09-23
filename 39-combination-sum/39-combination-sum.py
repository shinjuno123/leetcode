class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # same number can be used for unlimited multiple times
        
        results = []
        
        def dfs(elements,start,target):

            if target == 0:
                results.append(elements.copy())
                return
            
            if target < 0:
                return
                
        
            for i in range(start,len(candidates)):
                dfs(elements+[candidates[i]], i, target-candidates[i])
            
        dfs([],0,target)
        
        return results
        
        