class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j, result  = 0, len(heights) - 1, 0

        while i < j:
            area = ( j - i ) * min(heights[i], heights[j])
            result = max(result, area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return result