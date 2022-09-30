from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        
        def findSub(index,sub):
        
            if s[index] in used:
                return
            
            for i in range(index,len(s)-1):
                if s[i] not in used:
                    used.add(s[i])
                    t = findSub(i+1, s[i+1])
                    sub += '' if t is None else t
                    break
                    
            return sub
        
        res = 0
        for i in range(len(s)):
            a = findSub(i,s[i])
            res = max(res,len(a))
            used.clear()
            
        
        return res