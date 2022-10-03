from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        table = defaultdict(list)
        for dpt,avl in tickets:
            table[dpt].append(avl)
            table[dpt].sort(reverse=True)
        
        res = []
            
        def dfs(departure):
        
            while table[departure]:
                dfs(table[departure].pop())
            
            res.append(departure)
        
        dfs("JFK")
        
        return res[::-1]
            
            