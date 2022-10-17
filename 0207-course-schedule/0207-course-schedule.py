class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        visited = set()
        
        def dfs(key):
            if key in visited:
                return True
            
            if key in traced:
                return False
            
            traced.add(key)
            for i in graph[key]:
                if not dfs(i):
                    return False
            
            traced.remove(key)
            visited.add(key)
            
            return True
            
            
        
        for key in list(graph):
            if not dfs(key):
                return False
            
        
        return True