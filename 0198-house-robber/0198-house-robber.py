class Solution:
    def rob(self, nums: List[int]) -> int:
        table = collections.defaultdict(int)
        def _rob(i):
            if i < 0:
                return 0
            if i in table:
                return table[i]
    
            table[i] = max(_rob(i - 1),_rob(i - 2) + nums[i])
            
            return table[i]
        
        return _rob(len(nums) - 1)