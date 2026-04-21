class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodemin = [math.inf] * (n + 1)
        nodemin[k], nodemin[0] = 0, 0
        edgelist = defaultdict(list)
        q = deque()
        q.append(k)

        for s,d,t in times:
            edgelist[s].append((d,t))


        while len(q):
            node = q.popleft()
            time = nodemin[node]

            for d, t in edgelist[node]:
                if nodemin[d] > time + t:
                    nodemin[d] = time + t
                    q.append(d)


        if max(nodemin) == math.inf:
            return -1
        else:
            return max(nodemin)







        