class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 
        left_max = 0
        right_max = 0
        res = 0
        
        while left < right:
            # get higher pillar height than original value on either side 
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            # if left pointer's max is not bigger than right pointer's, then get trapped rain waer and increment left 
            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
            # if right pointer's max is smaller than left pointer's, then get trapped rain water and decrement right
            else:
                res += right_max - height[right]
                right -= 1
        
        
        return res