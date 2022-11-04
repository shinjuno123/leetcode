class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i,v in enumerate(numbers):
            compliment = target - v
            idx1 = bisect.bisect_left(numbers[i+1:],compliment)
            if idx1 < len(numbers[i+1:]) and numbers[i + idx1 + 1] == compliment:
                return [i+1, idx1 + i + 2]
        