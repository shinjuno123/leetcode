import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = math.ceil(len(nums) / 2)
        counter = collections.Counter(nums)
        for key, val in counter.most_common():
            if val >= count:
                return key