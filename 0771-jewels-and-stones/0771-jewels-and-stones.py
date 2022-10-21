class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = collections.Counter(stones)
        
        res = 0
        for stone in stones:
            if stone in jewels:
                res += stones[stone]
        
        
        return res