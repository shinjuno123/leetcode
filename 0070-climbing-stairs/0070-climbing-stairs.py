class Solution:
    def climbStairs(self, n: int) -> int:
        table = collections.defaultdict(int)
        
        def fib(n):
            if n <= 1:
                return n
            if table[n]:
                return table[n]
            
            table[n] = fib(n - 1) + fib(n - 2)
            return table[n]
        
        return fib(n + 1)