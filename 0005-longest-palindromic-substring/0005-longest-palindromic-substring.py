class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            # if s[left] == s[right] is not same then return an empty string
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        
        # when length of the string is 1
        if len(s) < 2 or s == s[::-1]:
            return s
    
        
        
        # initialize a string to assign the longest substring to it
        maxsize_string = ""
        
        # loop over the string with iterating variable i
        for i in range(len(s) - 1):
            # expand the interval between left and right by incrementing right and decrementing left and also consider odd and even length of s
            maxsize_string = max(expand(i, i+2), expand(i, i+1),maxsize_string, key=len)
            
        
        
        # return maxsize_string
        return maxsize_string
        
        
        
    
        
        