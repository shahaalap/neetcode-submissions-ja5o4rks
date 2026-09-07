class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)


        while q:
            node = q.pop()
            if node >= len(nums) - 1:
                return True

            for i in range(nums[node]):
                if node + i + 1 not in visited:
                    q.append(node + i + 1)
                    visited.add(node + i + 1)
        

        return False