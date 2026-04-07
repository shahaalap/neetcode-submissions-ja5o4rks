class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()

        def bfs():
            
            visited = [[False] * n for _ in range(m)]

            while q:
                val1, val2, path = q.popleft()

                visited[val1][val2] = True

                if grid[val1][val2] == 2147483647:
                    grid[val1][val2] = path

                if val1 > 0 and not visited[val1 - 1][val2] and grid[val1 - 1][val2] != -1:
                    q.append((val1 - 1, val2, path + 1 ))
                if val1 < m - 1 and not visited[val1 + 1][val2] and grid[val1 + 1][val2] != -1:
                    q.append((val1 + 1, val2, path + 1))
                if val2 > 0 and not visited[val1][val2 - 1] and grid[val1][val2 - 1] != -1:
                    q.append((val1, val2 - 1, path + 1))
                if val2 < n - 1 and not visited[val1][val2 + 1] and grid[val1][val2 + 1] != -1:
                    q.append((val1, val2 + 1, path + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        bfs()
                    
        


