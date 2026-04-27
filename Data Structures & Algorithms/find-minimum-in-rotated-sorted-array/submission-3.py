class Solution:
    def findMin(self, nums: List[int]) -> int:
        i , j = 0, len(nums) - 1
        result = 1001

        while i <= j:
            mid = i + (j - i)//2
            result = min(result, nums[mid])

            if nums[mid] <= nums[j]:
                j = mid - 1
            else:
                i = mid + 1

        return result
        
            
