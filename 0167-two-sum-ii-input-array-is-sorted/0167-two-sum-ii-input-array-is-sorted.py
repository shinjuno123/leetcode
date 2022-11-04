class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,v in enumerate(numbers):
            expected = target - v
            left, right = i + 1, len(numbers) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if numbers[mid] > expected:
                    right = mid - 1
                elif numbers[mid] < expected:
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]
        