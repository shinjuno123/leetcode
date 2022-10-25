class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b  in prerequisites:
            graph[a].append(b)
        
        checked = set()
        visited = set()
        
        def dfs(sub):
            if sub in checked:
                return False
            
            if sub in visited:
                return True
            
            checked.add(sub)
            
            for i in graph[sub]:
                if not dfs(i):
                    return False
            
            checked.remove(sub)
            visited.add(sub)
            
            return True
        
        for key in list(graph):
            if not dfs(key):
                return False
        
        return True
            