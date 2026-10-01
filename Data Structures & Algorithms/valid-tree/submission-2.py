class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i: [] for i in range(n)}

        # builds the adjacency list
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, parent ):
          
            if node in visited:
                return False

            visited.add(node)

            for next_node in graph[node]:
                if next_node == parent:
                    continue

                if dfs(next_node, node) == False:
                    return False

            return True
            
        if dfs(n-1, -1) == False:
            return False
        
        return len(visited) == n

        
        