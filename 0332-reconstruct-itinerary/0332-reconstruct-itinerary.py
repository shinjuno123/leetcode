class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        res = []
        
        for dpt, avl in sorted(tickets,reverse=True):
            graph[dpt].append(avl)
        
        def dfs(depart):
            while graph[depart]:
                dfs(graph[depart].pop())
            
            res.append(depart)
        
        dfs("JFK")
        
        return res[::-1]