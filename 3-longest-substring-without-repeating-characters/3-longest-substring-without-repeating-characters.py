from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        
        def findSub(index,sub):
            if s[index] in used:
                return ''
            
            
            if s[index] not in used and index < len(s) -1:
                used.add(s[index])
                sub += findSub(index+1, s[index+1])
            
                    
            return sub
        
        res = 0
        for i in range(len(s)):
            a = findSub(i,s[i])
            # print(a)
            res = max(res,len(a))
            used.clear()
            
        
        return res