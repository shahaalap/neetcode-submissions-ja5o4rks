class Solution:
    def climbStairs(self, n: int) -> int:
        climb = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                climb[i] = 1
            elif i == 2:
                climb[i] = 2
            else:
                climb[i] = climb[i - 1] + climb[i - 2]
        
        return climb[n]

