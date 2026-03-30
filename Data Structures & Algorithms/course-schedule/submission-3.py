class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = [[] for _ in range(numCourses)]
        outgoing = [[] for _ in range(numCourses)]

        for node, dep in prerequisites:
            incoming[node].append(dep)
            outgoing[dep].append(node)

        q = deque()
        visited = [False] * numCourses
        for node in range(numCourses):
            if len(incoming[node]) == 0:
                q.append(node)
                visited[node] = True


        while q:
            node = q.pop()
            for dep in outgoing[node]:
                if not visited[dep] and all([visited[i] for i in incoming[dep]]):
                    q.append(dep)
                    visited[dep] = True

        return all(visited)
            