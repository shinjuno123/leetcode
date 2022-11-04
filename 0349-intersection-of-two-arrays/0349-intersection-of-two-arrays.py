class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        res = set()
        
        while nums1:
            set1.add(nums1.pop())
        
        for num in nums2:
            if num in set1:
                res.add(num)
        
        res = list(res)
        
        return res