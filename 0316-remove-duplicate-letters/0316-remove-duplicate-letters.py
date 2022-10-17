class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c_s = collections.Counter(s)
        print(c_s)
        
        stack = []
        check = set()
        
        for c in s:
            c_s[c] -= 1
            
            if c in check:
                continue
            
            while stack and stack[-1] > c and c_s[stack[-1]] > 0:
                check.remove(stack.pop())
            
            stack.append(c)
            check.add(c)
        
        
        
        return ''.join(stack)