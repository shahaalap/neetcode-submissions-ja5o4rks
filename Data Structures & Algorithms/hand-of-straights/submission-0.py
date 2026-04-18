class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        n = len(hand)
        visited = [False] * n

        def dfs(i,slate):
            if len(slate) == groupSize:
                return True
            
            if i == n:
                return False
            
            if visited[i]:
                return dfs(i + 1, slate)

            if slate[-1] == hand[i]:
                return dfs(i + 1, slate)
            elif hand[i] == slate[-1] + 1:
                visited[i] = True
                slate.append(hand[i])
                return dfs(i + 1,slate)
            else:
                return False


        for i in range(n):
            if not visited[i]:
                visited[i] = True
                if not dfs(i,[hand[i]]):
                    return False


        return all(visited)