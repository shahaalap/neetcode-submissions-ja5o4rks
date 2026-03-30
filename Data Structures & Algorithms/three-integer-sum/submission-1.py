class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            target = -n

            j, k = i + 1, len(nums) - 1
            while j < k:
                curval = nums[j] + nums[k]
                if curval == target:
                    result.append([n, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif curval < target:
                    j += 1
                else:
                    k -= 1
        
        return result



        