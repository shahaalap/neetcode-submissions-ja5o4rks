class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque()
        visited = [False] * len(nums)
        q.append((0,0))
        visited[0] = True

        while len(q):
            count = len(q)

            i , jump = q.popleft()
            steps = nums[i]

            if i == len(nums) - 1:
                return jump
            
            for _ in range(count):
                for j in range(1, steps + 1):
                    if i + j < len(nums) and not visited[i + j]:
                        visited[i + j] = True
                        q.append((i + j, jump + 1))
                


