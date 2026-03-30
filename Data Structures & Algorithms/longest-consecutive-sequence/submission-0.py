class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setofnums = set(nums)
        result = 0

        for n in nums:
            if n - 1 in setofnums:
                continue
            else:
                currentmax = 1
                i = n
                while i + 1 in setofnums:
                    currentmax += 1
                    i += 1
                
                result = max(result, currentmax)
        
        return result