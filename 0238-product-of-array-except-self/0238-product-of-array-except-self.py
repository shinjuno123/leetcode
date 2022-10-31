class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        start = 1
        
        for i in range(len(nums)):
            result.append(start)
            
            start *= nums[i]
        
        
        start = 1
        
        for i in range(len(nums) - 1,-1, -1):
            result[i] *= start
            start *= nums[i]
        
        
        return result
        
            
        
    