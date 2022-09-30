from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        
        for index, character in enumerate(s):
            
            # when meeting overlapping char
            if character in used and start <= used[character]:
                start = used[character] + 1
            else:
                max_length = max(max_length, index - start + 1)
            
            
            used[character] = index
        
        
        return max_length