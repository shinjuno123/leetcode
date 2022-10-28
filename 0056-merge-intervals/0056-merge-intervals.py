class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        stack = []
        
        for a, b in intervals:
            if stack and stack[-1][1] >= a and stack[-1][1] <= b:
                prev_a, prev_b = stack.pop()
                stack.append([prev_a, b])
                continue
            
            if stack and stack[-1][0] <= a and stack[-1][1] >= b:
                prev_a, prev_b = stack.pop()
                stack.append([prev_a,prev_b])
                continue
            
            if stack and stack[-1][0] >= a and stack[-1][1] <= b:
                prev_a, prev_b = stack.pop()
                stack.append([a,b])
                continue
            
            stack.append([a, b])
        
        return stack
            
            