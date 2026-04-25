class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgelist = [[] for _ in range(n)]
        result = 0
        visited = [False] * n

        for src, dst in edges:
            edgelist[src].append(dst)
            edgelist[dst].append(src)


        def bfs(i):
            q = deque()
            q.append(i)

            while len(q):
                node = q.popleft()

                for nei in edgelist[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

        for i in range(n):
            if not visited[i]:
                result += 1
                visited[i] = True
                bfs(i)


        return result