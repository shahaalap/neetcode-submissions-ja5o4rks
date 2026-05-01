class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for _ in range(n)]
        for fromi, toi, price in flights:
            adjList[fromi].append([toi,price])

        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        q = deque()
        q.append((src, 0, 0))

        while len(q):
            node, cost, stop = q.popleft()
            
            if node == dst:
                continue
            
            if stop > k:
                continue

            for nei, neip in adjList[node]:
                newcost = cost + neip
                if prices[nei] > newcost:
                    prices[nei] = newcost
                    q.append((nei, newcost, stop + 1))

        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]


            





        