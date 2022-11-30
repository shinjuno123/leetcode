class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary variable "anagrams" initialized with list at each key
        anagrams = collections.defaultdict(list)
        
        # loop over the given list, word by word
        for word in strs:
            # in each iteration, sort each word lexicograpghically
            # set sorted word as a key in anagrams
            # append original word in the list of the key
            anagrams[''.join(sorted(word))].append(word)
        
        # convert anagrams into list and return it
        return anagrams.values()