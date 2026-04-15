class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        half = sum(nums) // 2
        if half != sum(nums) / 2:
            return False
        
        cache = [[None] * (half + 1) for _ in range(len(nums))]


        def helper(i, total):    
            if total > half:
                return False

            if i == len(nums):
                return False

            if cache[i][total] != None:
                return cache[i][total]
            
            result = False        
            if total == half:
                result = True
            else:
                exclude = helper(i + 1, total)
                include = helper(i + 1, total + nums[i])

                result = False
                if exclude or include:
                    result = True

            cache[i][total] = result
            return result


        return helper(0, 0)