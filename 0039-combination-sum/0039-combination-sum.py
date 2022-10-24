class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(elements,target,start):

            if target == 0:
                res.append(elements)
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                dfs([candidates[i]] + elements, target - candidates[i], i)
            
            
        dfs([],target,0)
            
        return res