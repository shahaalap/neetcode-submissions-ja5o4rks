class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque([(i,j, 0)])
            visited = [[False] * n for _ in range(m)]

            while q:
                val1, val2, path = q.popleft()

                visited[val1][val2] = True

                if grid[val1][val2] == 0:
                    return path

                if val1 > 0 and not visited[val1 - 1][val2] and grid[val1 - 1][val2] != -1:
                    q.append((val1 - 1, val2, path + 1 ))
                if val1 < m - 1 and not visited[val1 + 1][val2] and grid[val1 + 1][val2] != -1:
                    q.append((val1 + 1, val2, path + 1))
                if val2 > 0 and not visited[val1][val2 - 1] and grid[val1][val2 - 1] != -1:
                    q.append((val1, val2 - 1, path + 1))
                if val2 < n - 1 and not visited[val1][val2 + 1] and grid[val1][val2 + 1] != -1:
                    q.append((val1, val2 + 1, path + 1))


            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    path = bfs(i, j)
                    if path > 0:
                        grid[i][j] = path
                    
        


