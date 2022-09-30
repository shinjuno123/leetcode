from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(list(stones))
        
        cnt = 0
        for jewel in jewels:
            if jewel in stones:
                cnt += counter[jewel]
        
        
        return cnt