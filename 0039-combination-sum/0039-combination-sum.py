class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        
        def dfs(start, target, elements):
            if target == 0:
                res.append(elements)
                return
            
            if target < 0:
                return
            
            for i in range(start,len(candidates)):
                dfs(i,target-candidates[i],[candidates[i]] + elements)
                
        
        dfs(0,target,[])
        
        return res