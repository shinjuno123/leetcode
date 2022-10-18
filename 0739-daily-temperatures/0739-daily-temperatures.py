class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i,temperature in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temperature:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)
            
        
        return res