import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # change all the letters into lowercase letters
        paragraph = paragraph.lower()
        # convert all non-alphabets to a space
        paragraph = re.sub("[^a-z]"," ",paragraph)
        # split them by a space.
        paragraph = paragraph.split()
        words = []
        # exclude banned words
        for word in paragraph:
            if word not in banned:
                words.append(word)
        # use counter function to count number of words occurs
        paragraph_counter = collections.Counter(words)
        
        # get most common word
        common_word = paragraph_counter.most_common()[0][0]
        
        # return the key
        return common_word