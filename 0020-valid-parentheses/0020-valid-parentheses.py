class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            ")":"(",
            "}":"{",
            "]":"[" 
        }
        
        stack = []
        
        for c in s:
            if stack and c in table and stack[-1] == table[c]:
                stack.pop()
                continue
            
            stack.append(c)

        return len(stack) == 0