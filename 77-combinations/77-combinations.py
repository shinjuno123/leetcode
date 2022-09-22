class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        prev_combination = []
        result = []
        
        def dfs(idx,nums):
            if len(nums) == n - k:
                result.append(prev_combination.copy())
                return
            
            print(idx)
            for i in range(idx, len(nums)):
                current_nums = nums.copy()
                current_nums.remove(nums[i])
                
                prev_combination.append(nums[i])
                
                dfs(i,current_nums)
                prev_combination.pop()
        
        
        dfs(0,nums)
        
        
        return result