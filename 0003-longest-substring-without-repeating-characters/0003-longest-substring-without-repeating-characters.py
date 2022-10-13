class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        start = 0
        max_l = 0
        
        for i, c in enumerate(s):
            if table and c in table and start <= table[c]:
                start = table[c] + 1
            else:
                max_l = max(max_l, i - start + 1)
            
            table[c] = i
            
        
        
        return max_l
        
        