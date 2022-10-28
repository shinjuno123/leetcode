import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p =  re.sub('[^a-z]',' ',paragraph.lower())
        counter = collections.Counter(p.split()).most_common()
 
        for word, count in counter:
            if not word in banned:
                return word
        
        return []