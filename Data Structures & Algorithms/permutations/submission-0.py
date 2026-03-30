class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, slate):
            if i == len(nums):
                result.append(slate[:])
                return

            for k in range(i, len(nums)):
                nums[i], nums[k] = nums[k], nums[i]
                slate.append(nums[i])
                helper(i + 1, slate)
                slate.pop()
                nums[i], nums[k] = nums[k], nums[i]

        helper(0, [])
        return result