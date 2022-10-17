class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for dpt, avl in sorted(tickets,reverse=True):
            graph[dpt].append(avl)
        
        
        res = []
        
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            
            res.append(airport)
            
        
        dfs("JFK")
        
        return res[::-1]