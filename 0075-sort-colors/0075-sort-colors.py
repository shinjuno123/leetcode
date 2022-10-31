class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 1
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] < mid:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > mid:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1
        
        
        return nums
        
        