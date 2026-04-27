class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def twosum(i, amount):
            j = len(nums) - 1
            twosumresults = []

            while i < j:
                counterpart = nums[i] + nums[j]
                if counterpart == amount:
                    twosumresults.append([nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif counterpart < amount:
                    i += 1
                else:
                    j -= 1
            
            return twosumresults

        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twosumresults = twosum(i + 1, -n)

            if twosumresults:
                for t in twosumresults:
                    t.append(n)
                    result.append(t)

        return result
