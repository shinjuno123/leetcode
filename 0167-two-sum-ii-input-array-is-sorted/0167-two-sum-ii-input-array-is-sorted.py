class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            idx1 = bisect.bisect_left(numbers[i+1:],compliment)
            if idx1 < len(numbers[i+1:]) and numbers[i+1:][idx1] == compliment:
                return [i+1, idx1 + i + 2]
        
        
        return
        