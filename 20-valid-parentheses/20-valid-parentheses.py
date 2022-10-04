class Solution:
    def isValid(self, s: str) -> bool:
        table = {")":"(",
                 "}":"{",
                 "]":"["}
        
        stack = []
        
        if len(s) <= 1:
            return False
        
        for letter in list(s):
            
            if stack and letter in table and stack[-1] == table[letter]:
                stack.pop()
                continue
                
            
            stack.append(letter)
    
        
        return not len(stack)