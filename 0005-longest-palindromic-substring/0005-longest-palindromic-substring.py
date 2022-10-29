class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            if left >= 0 and right <= len(s) - 1 and s[left] != s[right]:
                return ""
            
            while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            
            return s[left: right + 1]
        
        res = ""
        
        for i in range(len(s)):
            res = max(res, expand(i,i), expand(i,i+1),key=len)
         
        
        
        return res
        
        