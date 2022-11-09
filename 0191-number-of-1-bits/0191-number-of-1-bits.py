class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        n = str(bin(n))[2:]
        for bit in n:
            if bit == "1":
                cnt += 1
        
        return cnt