class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        minutes = -1
        countoffresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    countoffresh += 1

        
        while q:
            size = len(q)
            minutes += 1
            while size:
                nodei, nodej = q.popleft()
                grid[nodei][nodej] = 2

                for ni,nj in neighbors:
                    nextnodei, nextnodej = nodei + ni, nodej + nj

                    if nextnodei < 0 or nextnodei >= n:
                        continue
                    if nextnodej < 0 or nextnodej >= m:
                        continue

                    if grid[nextnodei][nextnodej] == 1 and not visited[nextnodei][nextnodej]:
                        q.append((nextnodei, nextnodej))
                        visited[nextnodei][nextnodej] = True

                size -= 1
        

        postcountfresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    postcountfresh += 1


        if countoffresh == 0:
            return 0
        elif postcountfresh > 0:
            return -1
        
        return minutes

