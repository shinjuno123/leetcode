class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary called dic
        dic = {}
        
        # loop over nums with interating variables num and index
        for i, num in enumerate(nums):
            # subtract num from target and get a complement
            complement = target - num
            # search for the complement in the dic and return the answer if complement exists in the dic as a key
            if complement in dic:
                return [dic[complement], i]
            
            # assign index number as a value and num as a key to dic
            dic[num] = i
        
        
        # there will be exactly one solution so no need for more return here
        
        
        