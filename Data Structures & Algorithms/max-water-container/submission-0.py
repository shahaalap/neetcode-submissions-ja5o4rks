class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        i , j = 0 , len(heights) - 1

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)

            result = max(result, area)

            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return result