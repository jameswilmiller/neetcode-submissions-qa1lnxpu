class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        components = 0
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        
        visited = set()

        def dfs(node):

            if node in visited:
                return

            visited.add(node)
            
            for next_node in adj[node]:
                dfs(next_node)
        

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components

                
        