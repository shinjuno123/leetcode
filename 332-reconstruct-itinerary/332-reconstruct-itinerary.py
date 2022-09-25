from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dic = defaultdict(list)
        
        result = []
        # 1. Change tickets into hashmap
        for ticket in tickets:
            tickets_dic[ticket[0]].append(ticket[1])
        
        for key in tickets_dic:
            tickets_dic[key].sort()
        
        # print(tickets_dic)
        
        def dfs(departure):
            while tickets_dic[departure]:
                dfs(tickets_dic[departure].pop(0))
            result.append(departure)
        
        
        dfs("JFK")
        return result[::-1]