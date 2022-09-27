class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for letter in sorted(set(s)):
            suffix = s[s.index(letter):]
            if set(s) == set(suffix):
                return letter + self.removeDuplicateLetters(suffix.replace(letter,''))
        
        return ''
            