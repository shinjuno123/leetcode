class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        
        stack = []
        found = set()
        
        for c in s:
            counter[c] -= 1
            
            
            if c in found:
                continue
            
            
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                found.remove(stack.pop())
            
            
            found.add(c)
            stack.append(c)
        
        
        return ''.join(stack)
            