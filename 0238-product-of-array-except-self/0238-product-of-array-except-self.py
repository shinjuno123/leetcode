class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize an empty array result
        result = []
        
        # initialize tmp with 1
        tmp = 1
        
        # iterate nums with iterating value num
        for num in nums:
            # push tmp into result
            result.append(tmp)
            # get product of tmp with num and add to original tmp
            tmp *= num
        
        # initalize tmp with 1 again
        tmp = 1
        
        # iterate nums backwards with iterating value i(index)
        for i in range(len(nums) - 1, -1, -1):
            # get result[i] * tmp and assign the value to result[i]
            result[i] *= tmp
            
            # get product of tmp with nums[i] and add to original tmp
            tmp *= nums[i]
        
        
        # return result
        return result