class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if not height:
            return result
            
        total = len(height)
        maxl = [0] * total
        maxr = [0] * total
        
        maxl[0] = 0
        for i in range(1, total):
            maxl[i] = max(maxl[i - 1], height[i-1])

        maxr[total - 1] = 0
        for j in range(total - 2, -1, -1):
            maxr[j] = max(maxr[j + 1], height[j + 1])

        for k in range(total):
            result += max(min(maxl[k], maxr[k]) - height[k], 0)

        return result
