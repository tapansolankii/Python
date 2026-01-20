from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
       
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1.0 / val))
        
        def dfs(start, end, visited):
           
            if start not in graph or end not in graph:
                return -1.0
    
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0

        results = []
        for c, d in queries:
            results.append(dfs(c, d, set()))
            
        return results