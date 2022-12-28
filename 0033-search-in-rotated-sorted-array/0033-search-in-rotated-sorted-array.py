class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0
        
        while left <= right:
            parent = (right - left) // 2 + left
            
            if nums[parent] > nums[right]:
                left = parent + 1
            elif nums[parent] < nums[right]:
                right = parent
            else:
                pivot = parent
                break
        

        left = pivot
        right = pivot - 1 + len(nums)
        
        while left <= right:
            parent = (right - left) // 2 + left
            actual_center = parent % len(nums)
            if nums[actual_center] > target:
                right = parent - 1
            elif nums[actual_center] < target:
                left = parent + 1
            else:
                return actual_center
        
        return -1
            
            
        
        