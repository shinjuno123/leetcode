class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = set()
    
        t = ''.join(sorted(list(t)))
        s = ''.join(sorted(list(s)))
        return t == s
        