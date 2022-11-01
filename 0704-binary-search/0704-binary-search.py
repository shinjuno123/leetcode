class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] < target:
                    return binarySearch(mid+1, right)
                elif nums[mid] > target:
                    return binarySearch(left, mid - 1)
                else:
                    return mid
                
            else:
                return -1
        
        
        
        return binarySearch(0, len(nums)-1)