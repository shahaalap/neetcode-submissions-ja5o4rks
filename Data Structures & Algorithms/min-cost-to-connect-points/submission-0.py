class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = [[0] * n for _ in range(n)]
        visited = [False] * n
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjList[i][j] = dist
                adjList[j][i] = dist


        minH = []
        heapq.heappush(minH, (0,0))

        while len(minH) > 0:
            cost, i = heapq.heappop(minH)
            if visited[i]:
                continue
            result += cost
            visited[i] = True

            for j in range(n):
                if not visited[j]:
                    heapq.heappush(minH,(adjList[i][j], j))

        return result



        