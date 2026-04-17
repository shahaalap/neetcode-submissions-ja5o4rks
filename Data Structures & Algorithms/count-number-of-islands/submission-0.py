class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        result = 0

        def bfs():
            while len(q):
                i, j = q.popleft()
                for ni,nj in neighbors:
                    nei, nej = i + ni, j + nj
                    if nei >= 0 and nei < n and nej >= 0 and nej < m and grid[nei][nej] == "1" and not visited[nei][nej]:
                        q.append([nei,nej])
                        visited[nei][nej] = True


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    result += 1
                    q.append([i,j])
                    bfs()

        return result
            