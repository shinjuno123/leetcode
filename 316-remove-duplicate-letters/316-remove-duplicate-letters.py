class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for letter in sorted(set(s)):
            suffix = s[s.index(letter):]
            if set(suffix) == set(s):
                return letter + self.removeDuplicateLetters(suffix.replace(letter,''))
        
        return ''
            