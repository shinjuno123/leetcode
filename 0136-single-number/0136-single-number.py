class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(0,len(nums),2):
            if i + 1 < len(nums) and nums[i] != nums[i+1]:
                return nums[i]
        
        
        return nums[-1]