class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        result = 0

        def bfs():
            while len(q):
                i, j = q.popleft()
                grid[i][j] = "0"
                for ni,nj in neighbors:
                    nei, nej = i + ni, j + nj
                    if nei >= 0 and nei < n and nej >= 0 and nej < m and grid[nei][nej] == "1":
                        q.append([nei,nej])


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    result += 1
                    q.append([i,j])
                    bfs()

        return result
            