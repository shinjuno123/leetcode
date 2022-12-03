class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort nums
        nums.sort()
        # sum first index of group(index n and index n + 1)
        return sum(nums[0::2])