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
                current_elements = elements.copy()
                current_elements.append(candidates[i])
                tar = target - candidates[i]
                dfs(current_elements,i,tar)
                current_elements.pop()
            
        dfs([],0,target)
        
        return results
        
        