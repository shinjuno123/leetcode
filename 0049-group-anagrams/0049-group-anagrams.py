class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        
        for word in strs:
            table[''.join(sorted(list(word)))].append(word)
        return table.values()
        
        
        