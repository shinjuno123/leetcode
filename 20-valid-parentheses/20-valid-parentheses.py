class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        dic = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        stck = []
        
        for p in s:
            if p not in dic:
                stck.append(p)
            elif not stck or dic[p] != stck.pop():
                return False
            
        return len(stck) == 0
            
    