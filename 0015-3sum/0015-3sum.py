class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[left] + nums[right] + nums[i]
                
                if sum_ > 0:
                    right -= 1
                
                if sum_ < 0:
                    left += 1
                
                if sum_ == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        
        return res