class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        
        nums2.sort() # nlogn
        
        # nlogn
        for num1 in nums1: # n
            i2 = bisect.bisect_left(nums2,num1) # logn
            if len(nums2) > 0 and len(nums2) > i2 and nums2[i2] == num1:
                result.add(num1)
        
        
        return list(result) # 2nlogn -> nlogn