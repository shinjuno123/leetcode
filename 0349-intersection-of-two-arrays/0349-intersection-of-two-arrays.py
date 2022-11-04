class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        
        nums2.sort()
        
        for num1 in nums1:
            i2 = bisect.bisect_left(nums2,num1)
            if len(nums2) > 0 and len(nums2) > i2 and nums2[i2] == num1:
                result.add(num1)
        
        
        return list(result)