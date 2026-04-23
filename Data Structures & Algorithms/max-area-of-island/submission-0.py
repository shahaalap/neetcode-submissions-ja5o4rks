class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area , n, m = 0, len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            currenarea = 0

            while len(q):
                nodei,nodej = q.popleft()
                currenarea += 1

                for nei,ney in neighbors:
                    x, y = nei + nodei, ney + nodej
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1 and not visited[x][y]:
                        visited[x][y] = True
                        q.append((x,y))

            return currenarea


        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    islandarea = bfs(i,j)
                    area = max(area, islandarea)


        return area

