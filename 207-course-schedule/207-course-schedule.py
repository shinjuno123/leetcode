class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        count = 0
        
        traced = set()
        visited = set()
        
        def dfs(subject):
            
            if subject in traced:
                return False
            
            if subject in visited:
                return True
            
            traced.add(subject)
            
            for sub in graph[subject]:
                if not dfs(sub):
                    return False
            
            traced.remove(subject)
            visited.add(subject)
            
            return True
        
        for sub in list(graph):
            if not dfs(sub):
                return False
        
        
        return True
        