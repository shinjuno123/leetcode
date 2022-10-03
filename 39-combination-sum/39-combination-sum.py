class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        
        def dfs(li,idx):
            if sum(li) == target:
                result.append(li[:])
                return
            
            if sum(li) > target:
                return
            
            for i in range(idx,len(candidates)):
                li.append(candidates[i])
                dfs(li,i)
                li.pop()
        
        
        
        
        dfs([],0)
        
        return result
        
        
        