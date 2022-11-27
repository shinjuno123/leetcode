import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '',s.lower())
        
        left = 0
        right = len(s) - 1
    
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        

        
        return left >= right