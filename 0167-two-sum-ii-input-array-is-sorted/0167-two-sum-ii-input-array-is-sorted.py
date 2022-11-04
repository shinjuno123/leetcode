class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i,v in enumerate(numbers):
            compliment = target - v
            idx1 = bisect.bisect_left(numbers,compliment,i+1)
            if idx1 < len(numbers) and numbers[idx1] == compliment:
                return [i+1, idx1 + 1]
        