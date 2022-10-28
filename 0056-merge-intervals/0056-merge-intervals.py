class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and merged[-1][1] >= i[0]:
                merged[-1][1] = max(merged[-1][1],i[1])
            else:
                merged.append(i)
        
        
        return merged
        
        
    
            
            