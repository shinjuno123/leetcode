class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums.sort()
        # initialize res with an empty list
        res = []
        
        # for iteration with iterating variable i that is index
        for i in range(len(nums)):
            # initialize left with i + 1 and initialize right with the end of the length of nums
            left = i + 1
            right = len(nums) - 1
            # if i is bigger than 0 and nums[i] and nums[i - 1] are same then continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            # while iteration until left pointer's is same to right pointer's
            while left < right:
                # get a sum of nums[i] + nums[left] + nums[right] elements
                sum_ = nums[i] + nums[left] + nums[right]
                # if sum_ is bigger than 0, then decrement right
                if sum_ > 0:
                    right -= 1
                # if sum_ is smaller than 0, then increment left
                elif sum_ < 0:
                    left += 1
                # when both are same, append nums[i], nums[left], nums[right] to res and skip duplicate elements
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    
                    # increment left and decrement right
                    left += 1
                    right -= 1
        
        
        
        # return res
        return res
                