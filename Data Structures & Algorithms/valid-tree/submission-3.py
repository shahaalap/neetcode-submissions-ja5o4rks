class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgelist = [[] for _ in range(n)]

        for x,y in edges:
            edgelist[x].append(y)
            edgelist[y].append(x)

        parents = {}
        visited = [False] * n

        def bfs(i):
            q = deque()
            q.append(i)
            parents[i] = -1

            while len(q):
                node = q.popleft()

                for nei in edgelist[node]:
                    if not visited[nei]:
                        q.append(nei)
                        parents[nei] = node
                        visited[nei] = True
                    elif parents[node] != nei:
                        return True

            return False


        islandcount = 0
        for i in range(n):
            if not visited[i]:
                if islandcount == 1:
                    return False

                islandcount += 1
                visited[i] = True
                iscycle = bfs(i)
                if iscycle:
                    return False


        return True

