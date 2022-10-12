class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = collections.Counter(stones)
        
        cnt = 0
        for jewel in jewels:
            cnt += stones[jewel]
        
        
        return cnt
        
        