class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def helper(i, slate):
            if i == n:
                result.append(slate[:])
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                slate.append(nums[i])
                helper(i + 1, slate)
                nums[i], nums[j] = nums[j], nums[i]
                slate.pop()
        
        helper(0, [])
        return result